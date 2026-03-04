🚀 VDownloader: Sosyal Medya İndirme Asistanı

VDownloader, favori içeriklerinizi saniyeler içinde cebinize getiren, Telegram tabanlı yüksek performanslı bir video indirme botudur. Karmaşık linklerle uğraşmak yerine, bağlantıyı bota gönderin ve gerisini ona bırakın!
✨ Öne Çıkan Özellikler

    Çoklu Platform Desteği: Instagram Reels ve Twitter (X) videolarını tek tıkla yakalayın.

    Hızlı & Kayıpsız: İçerikleri orijinal kalitesinde ve en hızlı şekilde indirin.

    Sunucu Odaklı: VPS veya ev sunucunuzda 7/24 kesintisiz çalışacak şekilde optimize edilmiştir.

    Docker Entegrasyonu: Karmaşık bağımlılıklarla uğraşmadan tek komutla kurulum.

🛠️ Kurulum ve Hazırlık

Botun kusursuz çalışması için aşağıdaki adımları sırasıyla takip edin:
1. Kimlik Bilgilerinin Hazırlanması

    Instagram Cookies: Instagram'ın botu engellememesi için tarayıcınızdan aldığınız cookies.txt dosyasını ana dizine eklemelisiniz.

    Telegram Bot Token: @BotFather üzerinden oluşturduğunuz API anahtarını hazırlayın.

    User ID: Botun sadece size hizmet etmesi için Telegram kullanıcı ID'nizi not alın.

2. Projenin Sunucuya Çekilmesi

Terminalinizi açın ve projeyi VPS'inize klonlayın:
Bash

git clone https://github.com/tunahancoban/video_downloader_bot.git
cd video_downloader_bot

3. Yapılandırma

docker-compose.yml dosyasını favori editörünüzle (nano/vim) açarak değişkenleri güncelleyin:
YAML

services:
  bot:
    environment:
      - TELEGRAM_BOT_TOKEN=buraya_token_gelecek
      - ALLOWED_USER_ID=buraya_id_gelecek

4. Çalıştırma 🚀

Her şey hazırsa Docker'ın gücünü arkamıza alalım:
Bash

docker-compose up -d

📖 Kullanım

Botu Telegram'da başlatın ve herhangi bir Instagram veya Twitter linkini bota gönderin. Video otomatik olarak işlenecek ve size medya dosyası olarak gönderilecektir.
