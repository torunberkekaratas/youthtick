# ✅ LOCAL SEO HIZLI BAŞLANGIÇ CHECKLİSTİ

## 🔴 KRİTİK (Bugün Yapılmalı)

### 1. NAP Bilgilerini Hazırlayın
- [ ] Tam ofis adresi (sokak + numara)
- [ ] Posta kodu (77100 veya farklı?)
- [ ] Telefon numarası (+90...)
- [ ] Çalışma saatleri (09:00-18:00?)

**ÖNEMLİ:** Bu bilgiler AYNI şekilde her yerde kullanılmalı!

---

### 2. Google Business Profile Oluşturun
🔗 **Link:** https://www.google.com/business/

**Doldurulacak Bilgiler:**
- [ ] Business Name: "YouthTICK Yalova Gençlik İnisiyatifi"
- [ ] Category: "Non-profit organization"
- [ ] Secondary Category: "Youth organization" + "Educational service"
- [ ] Address: [Yukarıda belirlediğiniz adres]
- [ ] Phone: [Yukarıdaki telefon]
- [ ] Website: https://youthtick.org
- [ ] Hours: Pazartesi-Cuma 09:00-18:00
- [ ] Description: (500 karakter, keyword-rich)

**Description Örneği:**
```
YouthTICK, Yalova merkezli gençlik inisiyatifidir. Yalova gençlerine ücretsiz Erasmus+ başvuru desteği, gençlik projesi danışmanlığı ve yabancı dil eğitimi sunuyoruz. 2026'dan bu yana Yalova'dan 47 genç Erasmus+ programlarına katıldı. Avrupa Gönüllü Hizmeti, gençlik değişimi ve sivil katılım projelerinde rehberlik sağlıyoruz. İngilizce, Almanca, İspanyolca dil kursları mevcuttur.
```

**Doğrulama:**
- [ ] Postcard verification (5-7 gün sürer)
- [ ] VEYA phone verification (hemen)

---

### 3. Logo & Fotoğraflar Yükleyin (GBP'ye)
- [ ] Logo: logoalt.png (512x512px)
- [ ] Cover Photo: hero-main.jpg (veya ofis dış görüntüsü)
- [ ] 5+ iç mekan fotoğrafı (ofis, toplantı odası, etkinlikler)
- [ ] Ekip fotoğrafları (varsa)

---

## 🟡 YÜKSEK ÖNCELİK (Bu Hafta)

### 4. Schema Güncellemesi (index.html)
**Dosya:** local-seo-schema-update.json

**Yapılacaklar:**
- [ ] Mevcut Organization schema'yı açın (index.html satır ~45-65)
- [ ] local-seo-schema-update.json içeriğini kopyalayın
- [ ] [BURAYA GERÇEK ADRESİNİZİ YAZIN] → Gerçek adresi yazın
- [ ] +90-XXX-XXX-XXXX → Gerçek telefonu yazın
- [ ] Geo coordinates'i kontrol edin (Yalova Merkez: 40.6556, 29.2769)
  - Eğer farklı bir mahallede iseniz, Google Maps'ten doğru koordinatları alın
- [ ] Kaydedin

**Koordinat Nasıl Bulunur:**
1. Google Maps'e git: https://www.google.com/maps
2. Adresinizi ara
3. Pin'e sağ tıkla → İlk satırdaki sayılar = lat, lon
4. Örnek: `40.6556, 29.2769`

---

### 5. Google Maps Embed Ekleyin
**Dosya:** google-maps-embed-template.html

**Adımlar:**
1. [ ] Google Maps'te adresinizi arayın
2. [ ] "Share" → "Embed a map" → iframe kodunu kopyalayın
3. [ ] google-maps-embed-template.html dosyasını açın
4. [ ] `[GOOGLE_MAPS_EMBED_URL]` yerine iframe src URL'i yapıştırın
5. [ ] Diğer placeholder'ları doldurun ([BURAYA TAM ADRESİNİZİ YAZIN] vs.)
6. [ ] Tüm section'ı kopyalayın
7. [ ] index.html'e yapıştırın (contact section'dan ÖNCE)

**Nereye yapıştırılacak:**
```html
<!-- Mevcut hero section -->
...
<!-- Yeni Google Maps Section BURAYA -->
<section class="google-maps-section">...</section>
<!-- Mevcut contact section -->
...
```

---

### 6. Diğer Platformlara Kayıt
- [ ] Bing Places: https://www.bingplaces.com
- [ ] Apple Maps: https://mapsconnect.apple.com
- [ ] Yandex Business: https://business.yandex.com.tr

**Her platformda AYNI NAP bilgilerini kullanın!**

---

## 🟢 ORTA ÖNCELİK (2-4 Hafta)

### 7. Review Collection Başlatın
- [ ] İlk 5 mutlu kullanıcıya email gönderin
- [ ] GBP review linki: `https://g.page/[your-business-name]/review`
- [ ] Email template hazırlayın:

```
Konu: YouthTICK deneyiminizi paylaşır mısınız? ⭐

Merhaba [İsim],

[Program Adı]'na katılımınızın üzerinden [X] hafta geçti. 
Umarız harika deneyimler yaşıyorsunuzdur!

YouthTICK'i gelecekteki gençlere önermek ister misiniz?
Google'da kısa bir yorum bırakarak bize yardımcı olabilirsiniz:

👉 [GBP Review Link]

Teşekkürler!
YouthTICK Ekibi
```

**Hedef:** 4 hafta içinde 10 review

---

### 8. Yeni İçerik Sayfaları Oluşturun

#### yalova-dil-kurslari.html
- [ ] Sayfa oluştur
- [ ] İçerik yaz (800+ kelime)
- [ ] EducationalOccupationalProgram schema ekle
- [ ] Internal linkler ekle

#### yalova-erasmus-success-stories.html
- [ ] 5-10 başarı hikayesi topla
- [ ] Her hikaye için Person schema
- [ ] Fotoğraflar ekle
- [ ] Video testimonials embed et (varsa)

---

### 9. Local Backlinks İçin Outreach

**İletişime Geçilecek Yerler:**
- [ ] Yalova Üniversitesi - Partnership teklifi
- [ ] Yalova Belediyesi Gençlik Merkezi - Etkinlik iş birliği
- [ ] Yalova yerel gazeteleri - Başarı hikayeleri basın bülteni
- [ ] Yalova liseleri - Bilgilendirme seminerleri teklifi

**Email Template:**
```
Konu: Yalova Gençlerine Erasmus+ Desteği - İş Birliği Teklifi

Sayın [İlgili Kişi],

YouthTICK olarak Yalova'da gençlere ücretsiz Erasmus+ başvuru 
desteği sunuyoruz. 2026'dan bu yana 47 genç programa yerleşti.

[Kurum] ile iş birliği yaparak:
- Öğrencilerinize ücretsiz bilgilendirme seminerleri verebiliriz
- Başvuru sürecinde 1:1 mentorluk sağlayabiliriz
- Ortak etkinlikler organize edebiliriz

Görüşmek ister misiniz?

Saygılarımla,
[İsim]
YouthTICK
info@youthtick.org
```

---

## 📊 TAKİP & ÖLÇÜM

### 10. Analytics Kurulumu
- [ ] Google Analytics 4'te "Yalova" segment oluştur
- [ ] Google Search Console'da "yalova erasmus" takibine başla
- [ ] GBP Insights'ı haftalık kontrol et

**Takip Edilecek Metrikler:**
- GBP views/month
- GBP actions (calls, website clicks, directions)
- "yalova erasmus" keyword ranking
- Reviews (count + avg rating)
- Organic traffic from Yalova

---

## ⏱️ TİMELİNE ÖZET

| Hafta | Yapılacaklar |
|-------|--------------|
| **1** | NAP belirle, GBP oluştur, Schema güncelle, Maps embed |
| **2** | Bing/Apple/Yandex kayıt, Dil kursları sayfası oluştur |
| **3** | İlk 10 review topla, Partner outreach başlat |
| **4** | Success stories sayfası, Backlink outreach |
| **5-8** | Review collection sürdür, İçerik genişlet, Optimize et |

---

## 🎯 BAŞARI KRİTERLERİ (3 Ay)

- [ ] GBP verified ve optimize
- [ ] 15+ reviews (4.5+ rating)
- [ ] "yalova erasmus" → Top 3
- [ ] 500+ GBP views/month
- [ ] 10+ local citations
- [ ] 3+ local backlinks
- [ ] 300+ organic visits from Yalova

---

## ❓ SORULAR?

**Telefon/Adres bulamıyorum:**
- Sanal ofis kiralayabilirsiniz (aylık ~500-1000 TL)
- VEYA: Yalova Üniversitesi'nden ortak çalışma alanı talep edebilirsiniz
- VEYA: VoIP telefon numarası alabilirsiniz (Bizcell, Netgsm gibi)

**GBP doğrulama yapamıyorum:**
- Postcard 5-7 gün sürer, bekleyin
- Video verification deneyebilirsiniz
- Google My Business support'tan yardım isteyin

**Review nasıl toplanır?**
- Mutlu müşterilere doğrudan link gönderin
- QR code oluşturup ofiste kullanın
- Email signature'a "Bizi değerlendirin" linki ekleyin

---

**🚀 ŞİMDİ BAŞLAYIN:**  
Yukarıdaki "KRİTİK" bölümü bugün tamamlayın!
