import os
import shutil
import glob
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Yapılandırma - Docker Compose ortam değişkenlerinden çekiliyor
TOKEN = os.environ.get("BOT_TOKEN")
# USER_ID değişkenini integer'a çeviriyoruz (Eğer tanımlıysa)
AUTHORIZED_USER_ID = os.environ.get("MY_ID")
if AUTHORIZED_USER_ID:
    AUTHORIZED_USER_ID = int(AUTHORIZED_USER_ID)

DOWNLOAD_DIR = "downloads"
SUPPORTED_EXTENSIONS = (".mp4", ".mkv", ".webm", ".mov")

def get_downloaded_file(target_dir):
    for ext in SUPPORTED_EXTENSIONS:
        files = glob.glob(os.path.join(target_dir, f"*{ext}"))
        if files:
            return files[0]
    return None

async def handle_error(update: Update, status_msg, exception):
    error_str = str(exception)
    print(f"❌ Hata Detayı: {error_str}")

    if any(key in error_str for key in ["Sign in", "401", "Forbidden", "Dependency"]):
        text = "❌ Erişim engellendi. cookies.txt dosyasını yenilemeniz veya bağımlılıkları (ffmpeg vb.) kontrol etmeniz gerekiyor."
    else:
        text = f"❌ Bir hata oluştu: {error_str[:100]}"

    await status_msg.edit_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Yetkili kullanıcı kontrolü
    if AUTHORIZED_USER_ID and update.effective_user.id != AUTHORIZED_USER_ID:
        return

    target_dir = os.path.join(DOWNLOAD_DIR, str(update.effective_chat.id))
    
    # Not: Burada indirme işlemini yapan (yt-dlp çağıran) kodun 
    # bu bloktan önce veya burada çalışması gerektiğini unutmayın.
    
    status_msg = await update.message.reply_text("⏳ İşleniyor...")

    try:
        # Video dosyasını bul
        file_path = get_downloaded_file(target_dir)

        if not file_path or not os.path.exists(file_path):
            await status_msg.edit_text("❌ Video dosyası bulunamadı.")
            return

        # Videoyu Gönder
        with open(file_path, 'rb') as video:
            await update.message.reply_video(
                video=video,
                caption="✅ Başarıyla indirildi.",
                supports_streaming=True
            )
        await status_msg.delete()

    except Exception as e:
        await handle_error(update, status_msg, e)

    finally:
        # Temizlik işlemi
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

def main():
    if not TOKEN:
        print("❌ HATA: BOT_TOKEN ortam değişkeni bulunamadı!")
        return

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    # Bot kurulumu (Docker'dan gelen TOKEN kullanılıyor)
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print(f"🚀 Bot aktif. Yetkili ID: {AUTHORIZED_USER_ID if AUTHORIZED_USER_ID else 'Herkes'}")
    app.run_polling()

if __name__ == "__main__":
    main()
