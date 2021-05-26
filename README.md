# rubx

RUBX bir Sosyal Mühendislik saldırı yöntemi olan Phishing(oltalama) saldırısı yardımcı aracıdır.

/sites dizininde bulunan site dosyaları ile güncel web uygulamalarını taklit edip, hedeften kullanıcı adı, şifre gibi datalar girilmesini bekler.
Ve hedef bilgileri girip formu gönderdiği an /datas dizininde web uygulamasının adı ile oluşan <uygulama_adi>.txt uzantılı dosyanın içeriğine 
kullanıcıdan alınan hassas bilgiler daha sonra ulaşılması için kaydedilir.

Ngrok localinizde çalıştırdığınız bir web server'ı port yönlendirmeye gerek duymadan public internete açmak için kullanılan başarılı bir tunneling servisidir.

Örneğin: "localhost:80" portunda çalışan bir web uygulamanız var ve bunu domain/hosting almadan yayınlayıp test etmek istiyorsunuz.
Ngrok ile "localhost:80" portunuzu direkt olarak rastgele verilen bir ngrok tüneline yansıtabilirsiniz.
TCP ile yayınladığınızda size "8.tcp.ngrok.io:4658" benzeri bir link çıkaracaktır bu linki browser'ınızda açtığınız anda localinizde çalışan web uygulamasına ulaşmaktasınız. Biz de projemizde gizlilik ve pratiklik adına bu servisi kullanacağız.

GEREKSİNİMLER :

- ngrok => terminalden "pip3 install pyngrok" komutunuz çalıştırarak kurabilirsiniz.
- php   => sistemde yüklü değilse "sudo apt install php7.4-cli" yazarak kurabilirsiniz.

Rubx.py dosyasını çalıştırıp program içerisinden kullanacağınız web uygulamasını seçerek server hazırlıklarını otomatik yaptırıp sistemi hazır hale getirebilirsiniz.
