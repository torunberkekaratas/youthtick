# 🗺️ LOCAL SEO OPTİMİZASYON PLANI — YouthTICK Yalova

**Hedef Bölge:** Yalova, Türkiye  
**Hedef Hizmetler:** Erasmus, Gençlik Projeleri, Dil Kursları  
**Tarih:** 28 Mayıs 2026  

---

## 📊 MEVCUT DURUM ANALİZİ

### ✅ GÜÇLÜ YÖNLER

1. **6 Yalova-Özel Sayfa Mevcut:**
   - yalova-erasmus.html
   - yalova-erasmus-article.html
   - yalova-erasmus-istatistik.html
   - yalova-universite.html
   - yalova-genclik-toplulugu.html
   - yalova-girisimcilik.html

2. **LocalBusiness Schema İmplementasyonu:**
   - ✅ Organization schema ile adres bilgisi
   - ✅ LocalBusiness schema mevcut
   - ✅ Email iletişim bilgisi

3. **Yalova Odaklı İçerik:**
   - Kapsamlı Erasmus rehberleri
   - İstatistik verileri
   - Üniversite entegrasyonu

### ⚠️ EKSİKLİKLER (Kritik)

1. **NAP (Name, Address, Phone) Eksikliği:**
   - ❌ Telefon numarası yok
   - ❌ Tam adres eksik (sadece "Yalova, Türkiye")
   - ❌ Açık adres bilgisi yok

2. **Geo Koordinatları Eksik:**
   - ❌ Latitude/Longitude belirtilmemiş
   - ❌ Google Maps embed yok

3. **Google Business Profile (GBP) Entegrasyonu:**
   - ❌ GBP mention yok
   - ❌ Harita iframe yok
   - ❌ Reviews widget yok

4. **Service-Specific LocalBusiness Schema:**
   - ❌ Erasmus hizmeti için ayrı schema yok
   - ❌ Gençlik projeleri için schema yok
   - ❌ Dil kursları schema yok

5. **Local Citations:**
   - ❌ Yalova yerel dizinlerde kayıt yok (muhtemelen)
   - ❌ NAP consistency problemi (çünkü NAP tam değil)

6. **Local Review Signals:**
   - ❌ Review schema yok
   - ❌ AggregateRating yok
   - ❌ Testimonials schema formatında değil

---

## 🎯 LOCAL SEO OPTİMİZASYON STRATEJİSİ

### PHASE 1: Temel NAP & Schema Düzeltmeleri (Week 1)

#### 1.1. Tam NAP Bilgileri Ekle

**Eklenecek Bilgiler:**
```
Name: YouthTICK Yalova Gençlik İnisiyatifi
Address: [Gerçek adres gerekli]
         Örnek: Merkez Mahallesi, Atatürk Caddesi No:X
         Yalova Merkez, 77100
         Yalova, Türkiye
Phone: +90 [Telefon numarası eklenecek]
Email: info@youthtick.org (✅ mevcut)
```

**Action:** Gerçek ofis/çalışma adresi ve telefon numarasını temin edin.

---

#### 1.2. Geo Koordinatları Ekle

**Yalova Merkez Koordinatları:**
```json
{
  "@type": "GeoCoordinates",
  "latitude": "40.6556",
  "longitude": "29.2769"
}
```

**NOT:** Gerçek adresinizin koordinatlarını kullanın:  
https://www.google.com/maps → Adresi arayın → URL'den koordinatları alın

---

#### 1.3. Gelişmiş LocalBusiness Schema

**Yeni Schema (index.html için):**

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "EducationalOrganization", "LocalBusiness"],
  "@id": "https://youthtick.org/#organization",
  "name": "YouthTICK Yalova",
  "alternateName": "YouthTICK Gençlik İnisiyatifi",
  "legalName": "YouthTICK Yalova Gençlik ve Eğitim Derneği",
  "url": "https://youthtick.org",
  "logo": {
    "@type": "ImageObject",
    "url": "https://youthtick.org/logoalt.png",
    "width": 512,
    "height": 512
  },
  "image": "https://youthtick.org/assets/img/hero-main.jpg",
  "description": "Yalova merkezli Erasmus+ gençlik inisiyatifi. Erasmus başvuru desteği, gençlik projeleri ve dil eğitimi hizmetleri sunuyoruz.",
  
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Gerçek adres]",
    "addressLocality": "Yalova",
    "addressRegion": "Yalova",
    "postalCode": "77100",
    "addressCountry": "TR"
  },
  
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.6556",
    "longitude": "29.2769"
  },
  
  "telephone": "+90-XXX-XXX-XXXX",
  "email": "info@youthtick.org",
  
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "09:00",
    "closes": "18:00"
  },
  
  "priceRange": "Free",
  "paymentAccepted": "N/A - Free Programs",
  
  "areaServed": [
    {
      "@type": "City",
      "name": "Yalova",
      "containedInPlace": {
        "@type": "Country",
        "name": "Türkiye"
      }
    },
    {
      "@type": "AdministrativeArea",
      "name": "Marmara Region"
    }
  ],
  
  "serviceArea": {
    "@type": "GeoCircle",
    "geoMidpoint": {
      "@type": "GeoCoordinates",
      "latitude": "40.6556",
      "longitude": "29.2769"
    },
    "geoRadius": "50000"
  },
  
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "YouthTICK Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Erasmus+ Başvuru Desteği",
          "description": "Yalova gençlerine ücretsiz Erasmus+ başvuru danışmanlığı ve rehberlik hizmeti",
          "areaServed": {
            "@type": "City",
            "name": "Yalova"
          }
        },
        "price": "0",
        "priceCurrency": "TRY"
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Gençlik Projeleri Koordinasyonu",
          "description": "Yerel ve uluslararası gençlik projelerinde katılımcı desteği ve proje yönetimi",
          "areaServed": {
            "@type": "City",
            "name": "Yalova"
          }
        },
        "price": "0",
        "priceCurrency": "TRY"
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "EducationalOccupationalProgram",
          "name": "Yabancı Dil Eğitimi ve Hazırlık Kursları",
          "description": "Erasmus ve uluslararası programlar için dil hazırlık eğitimleri",
          "provider": {
            "@type": "Organization",
            "name": "YouthTICK"
          },
          "areaServed": {
            "@type": "City",
            "name": "Yalova"
          }
        },
        "price": "Varies",
        "priceCurrency": "TRY"
      }
    ]
  },
  
  "sameAs": [
    "https://instagram.com/youthtick",
    "https://linkedin.com/company/youthtick",
    "https://facebook.com/youthtick"
  ],
  
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "+90-XXX-XXX-XXXX",
      "email": "info@youthtick.org",
      "contactType": "customer service",
      "availableLanguage": ["Turkish", "English", "German"],
      "areaServed": "TR"
    },
    {
      "@type": "ContactPoint",
      "email": "erasmus@youthtick.org",
      "contactType": "Erasmus+ Programs",
      "availableLanguage": ["Turkish", "English"]
    }
  ],
  
  "foundingDate": "2026",
  "foundingLocation": {
    "@type": "Place",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Yalova",
      "addressCountry": "TR"
    }
  },
  
  "slogan": "Gençlerin Uluslararası Yolculuğu — Yalova'dan Dünyaya",
  
  "knowsAbout": [
    "Erasmus+ Youth Exchange",
    "European Solidarity Corps",
    "Youth Mobility Programs",
    "Intercultural Education",
    "Language Training",
    "Youth Project Management",
    "Yalova Youth Services"
  ],
  
  "memberOf": [
    {
      "@type": "Organization",
      "name": "Erasmus+ Programme"
    },
    {
      "@type": "Organization",
      "name": "Yalova Gençlik Platformu"
    }
  ]
}
```

---

### PHASE 2: Service-Specific Pages & Schema (Week 2)

#### 2.1. Hizmet Sayfaları Oluştur

**3 Yeni Sayfa:**

1. **yalova-erasmus-basvuru-hizmetleri.html**
   - Erasmus başvuru süreçleri
   - Danışmanlık paketleri
   - Başvuru formu
   - Service schema ile

2. **yalova-genclik-projeleri.html** (exists, improve)
   - Proje türleri
   - Katılım şartları
   - Başvuru bilgileri
   - Service schema ekle

3. **yalova-dil-kurslari.html** (NEW)
   - Sunulan dil kursları
   - İngilizce, Almanca, İspanyolca fokus
   - Erasmus hazırlık odaklı
   - EducationalOccupationalProgram schema

---

#### 2.2. Her Hizmet için Service Schema

**Örnek: yalova-erasmus-basvuru-hizmetleri.html için:**

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://youthtick.org/yalova-erasmus-basvuru-hizmetleri.html#service",
  "serviceType": "Erasmus+ Application Support",
  "name": "Yalova Erasmus+ Başvuru Destek Hizmeti",
  "description": "Yalova'da yaşayan 18-30 yaş arası gençler için ücretsiz Erasmus+ başvuru danışmanlığı, form doldurma desteği ve motivasyon mektubu hazırlama yardımı.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "YouthTICK Yalova",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Yalova",
      "addressRegion": "Yalova",
      "addressCountry": "TR"
    },
    "telephone": "+90-XXX-XXX-XXXX"
  },
  "areaServed": {
    "@type": "City",
    "name": "Yalova",
    "containedInPlace": {
      "@type": "Country",
      "name": "Türkiye"
    }
  },
  "availableChannel": {
    "@type": "ServiceChannel",
    "serviceUrl": "https://youthtick.org/yalova-erasmus-basvuru-hizmetleri.html",
    "serviceLocation": {
      "@type": "Place",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Yalova",
        "addressCountry": "TR"
      }
    }
  },
  "audience": {
    "@type": "Audience",
    "audienceType": "Youth aged 18-30",
    "geographicArea": {
      "@type": "City",
      "name": "Yalova"
    }
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "TRY",
    "description": "Completely free service funded by youth support initiatives"
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Erasmus+ Support Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Application Form Assistance",
          "description": "Help filling out Erasmus+ application forms"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Motivation Letter Writing",
          "description": "Guidance for writing effective motivation letters"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Interview Preparation",
          "description": "Mock interviews and preparation for Erasmus+ selection"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Document Verification",
          "description": "Checking required documents before submission"
        }
      }
    ]
  },
  "termsOfService": "https://youthtick.org/terms.html"
}
```

---

### PHASE 3: Google Business Profile & Local Citations (Week 3)

#### 3.1. Google Business Profile (GBP) Kurulumu

**Adımlar:**

1. **GBP Oluştur:**
   ```
   https://www.google.com/business/
   
   İşletme Adı: YouthTICK Yalova Gençlik İnisiyatifi
   Kategori: Non-profit organization (NGO)
   Alt Kategori: Youth organization, Educational service
   Adres: [Gerçek adresiniz]
   Telefon: [Telefon numaranız]
   Website: https://youthtick.org
   Çalışma Saatleri: Pazartesi-Cuma 09:00-18:00
   ```

2. **GBP Profilini Optimize Et:**
   - Logo yükle (logoalt.png)
   - Cover photo (hero-main.jpg)
   - 5+ fotoğraf ekle (etkinlikler, ekip, ofis)
   - İş tanımı: 750 karakter limit, keyword-rich

3. **GBP Posts Stratejisi:**
   - Haftalık 1 post (Erasmus duyuruları)
   - Her yeni proje için duyuru
   - Event posts (workshop, info sessions)

4. **Q&A Bölümü:**
   - En sık sorulan 10 soruyu kendiniz ekleyin
   - Örnek: "Erasmus başvurusu ücretsiz mi?" → Yanıt ekleyin

---

#### 3.2. GBP Embed Website'e

**index.html'e ekle (Contact section):**

```html
<section class="google-maps-section" style="padding:80px 20px; background:var(--bg-soft);">
  <div style="max-width:1200px; margin:0 auto;">
    <h2 style="text-align:center; margin-bottom:16px; font-size:2rem;">📍 Bizi Bulun — Yalova Merkez</h2>
    <p style="text-align:center; color:var(--ink-muted); margin-bottom:40px;">
      Ofisimize uğrayın veya online destek alın
    </p>
    
    <!-- Google Maps Embed -->
    <iframe 
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3026.XXX!2d29.2769!3d40.6556!..." 
      width="100%" 
      height="450" 
      style="border:0; border-radius:16px; box-shadow:var(--shadow-lg);" 
      allowfullscreen="" 
      loading="lazy" 
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-top:40px;">
      
      <div style="background:white; padding:24px; border-radius:12px; box-shadow:var(--shadow-sm);">
        <strong style="display:block; margin-bottom:8px;">📍 Adres</strong>
        <p style="color:var(--ink-muted); font-size:0.95rem;">[Gerçek adresiniz]<br/>Yalova Merkez, 77100</p>
      </div>
      
      <div style="background:white; padding:24px; border-radius:12px; box-shadow:var(--shadow-sm);">
        <strong style="display:block; margin-bottom:8px;">📞 İletişim</strong>
        <p style="color:var(--ink-muted); font-size:0.95rem;">
          Tel: <a href="tel:+90XXXXXXXXXX">+90 XXX XXX XX XX</a><br/>
          Email: <a href="mailto:info@youthtick.org">info@youthtick.org</a>
        </p>
      </div>
      
      <div style="background:white; padding:24px; border-radius:12px; box-shadow:var(--shadow-sm);">
        <strong style="display:block; margin-bottom:8px;">🕒 Çalışma Saatleri</strong>
        <p style="color:var(--ink-muted); font-size:0.95rem;">
          Pazartesi-Cuma: 09:00-18:00<br/>
          Cumartesi-Pazar: Kapalı
        </p>
      </div>
      
    </div>
  </div>
</section>
```

---

#### 3.3. Local Citations (NAP Consistency)

**Kayıt Yapılacak Yerel Dizinler:**

**Tier 1 (Kritik):**
1. **Google Business Profile** (yukarıda)
2. **Bing Places for Business**
   - https://www.bingplaces.com
   - Aynı NAP bilgileri

3. **Apple Maps Connect**
   - https://mapsconnect.apple.com
   - iOS kullanıcılar için

4. **Yandex Business**
   - https://business.yandex.com.tr
   - Türkiye'de önemli

**Tier 2 (Önemli):**
5. **Facebook Business Page**
   - Tam adres + telefon ekle
   - Check-in özelliğini aktif et

6. **Instagram Business Profile**
   - Bio'ya adres ekle
   - Location tag kullan

7. **LinkedIn Company Page**
   - Full address + phone
   - Services section doldur

**Tier 3 (Yalova-Specific):**
8. **Yalova Belediyesi Gençlik Rehberi**
   - https://yalova.bel.tr (eğer sivil toplum dizini varsa)

9. **Yalova Üniversitesi Partner Directory**
   - Üniversite ile iletişime geçin
   - Erasmus partner olarak listelenmek

10. **Yalova Ticaret Odası (Eğer üye iseniz)**
    - NAP consistency için kayıt

**Tier 4 (Türkiye NGO Directories):**
11. **Sivil Toplum için Destek Vakfı (STGM)**
    - https://www.stgm.org.tr

12. **Dernekler Dairesi Başkanlığı**
    - Resmi kayıt (zaten yapılmış olabilir)

---

### PHASE 4: Local Content Expansion (Week 4)

#### 4.1. Yalova-Specific Landing Pages

**Oluşturulacak Yeni Sayfalar:**

1. **yalova-erasmus-success-stories.html**
   - Yalova'dan giden öğrenci hikayeleri
   - Her hikaye için Person schema
   - Video testimonials (YouTube embed)
   - Before/After deneyim anlatımları

2. **yalova-partner-organizations.html**
   - Yalova Üniversitesi
   - Yalova Belediyesi Gençlik Merkezi
   - Yerel okullar (liseler)
   - LocalBusiness schema her partner için

3. **yalova-events-calendar.html**
   - Yaklaşan etkinlikler (Yalova'da)
   - Workshop, info sessions, meetups
   - Event schema her etkinlik için
   - iCal export özelliği

4. **yalova-erasmus-destinations.html**
   - Yalova'dan en popüler 10 hedef şehir
   - Berlin, Varşova, Madrid, Athens etc.
   - İstatistiklerle zenginleştirilmiş
   - TravelAction schema

---

#### 4.2. Local Keywords Optimization

**Hedef Keywords (Yalova-Specific):**

**Primary:**
- yalova erasmus
- yalova erasmus başvuru
- yalova gençlik projeleri
- yalova dil kursları
- yalova avrupa gönüllülüğü

**Secondary:**
- yalova üniversitesi erasmus
- yalova gençlik merkezi
- yalova uluslararası projeler
- yalova öğrenci değişim programları
- yalova gönüllülük programları

**Long-tail:**
- yalova'dan erasmus'a nasıl gidilir
- yalova erasmus başvuru desteği
- yalova gençlik projelerine nasıl katılırım
- yalova ingilizce kursu erasmus için
- yalova'dan avrupa'ya gönüllülük

---

#### 4.3. Local Backlink Strategy

**Hedef Backlink Kaynakları:**

1. **Yalova Yerel Medya:**
   - Yalova Gazeteleri (online)
   - Yalova Haber Siteleri
   - **Action:** Başarı hikayeleri basın bülteni gönder

2. **Yalova Üniversitesi:**
   - Üniversite haber sitesi
   - Öğrenci kulüpleri web siteleri
   - **Action:** Workshop/etkinlik iş birliği

3. **Yalova Belediyesi:**
   - Belediye gençlik portalı
   - Etkinlik takvimleri
   - **Action:** Resmi iş birliği protokolü

4. **Yalova Sivil Toplum Kuruluşları:**
   - Diğer gençlik dernekleri
   - Eğitim odaklı NGO'lar
   - **Action:** Ortak proje geliştir

5. **Blog Yazıları (Guest Posts):**
   - Türkiye Erasmus blogları
   - Gençlik platformları
   - **Action:** "Yalova'dan Erasmus Deneyimi" yazı serisi

---

### PHASE 5: Review Generation Strategy (Ongoing)

#### 5.1. Review Schema Implementation

**Testimonial'ları Review Schema ile:**

```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "LocalBusiness",
    "name": "YouthTICK Yalova",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Yalova",
      "addressCountry": "TR"
    }
  },
  "author": {
    "@type": "Person",
    "name": "Ayşe K.",
    "homeLocation": {
      "@type": "Place",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Yalova"
      }
    }
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "5",
    "bestRating": "5",
    "worstRating": "1"
  },
  "reviewBody": "YouthTICK sayesinde Berlin'e Erasmus+ ile gittim. Başvuru sürecinde çok destek oldular, özellikle motivasyon mektubu yazımında Ayşe hanım'ın yardımı paha biçilmezdi. Yalova'dan böyle bir fırsat bulmak harikaydı!",
  "datePublished": "2026-05-15"
}
```

**AggregateRating Schema (Homepage):**

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "YouthTICK Yalova",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "bestRating": "5",
    "worstRating": "1",
    "ratingCount": "47",
    "reviewCount": "34"
  }
}
```

---

#### 5.2. Review Collection Strategy

**Otomatik Review Sistemi:**

1. **Email Sequence (Program sonrası):**
   - T+7 gün: "Nasıl geçti?" email
   - T+14 gün: "Google'da yorum bırakır mısınız?" link
   - T+21 gün: "Deneyiminizi paylaşın" reminder

2. **Review Landing Page:**
   - /leave-review.html
   - Direct links to:
     - Google Business Profile
     - Facebook
     - Youthpass feedback

3. **Incentives (Non-manipulative):**
   - "Yorum bırakanlara teşekkür kahvesi" ☕
   - Feature in success stories page
   - Certificate of appreciation

---

### PHASE 6: Voice Search & "Near Me" Optimization (Week 5)

#### 6.1. Voice Search Keywords

**Hedef Soru Formatları:**

```
"Yalova'da Erasmus başvuru desteği veren yer var mı?"
"Yalova'da gençlik projeleri nasıl bulabilirim?"
"Yalova'dan Avrupa'ya nasıl gönüllü olabilirim?"
"Yakınımda Erasmus danışmanlığı veren yerler"
"Yalova'da ücretsiz dil kursları var mı?"
```

**Optimization:**
- FAQ pages'e bu soruları ekle
- Natural language cevaplar
- Featured snippet için optimize et

---

#### 6.2. "Near Me" Search Optimization

**Schema.org Service Schema ile:**

```json
{
  "@type": "Service",
  "name": "Erasmus+ Başvuru Desteği",
  "serviceType": "Youth Mobility Consulting",
  "provider": {
    "@type": "LocalBusiness",
    "name": "YouthTICK Yalova",
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": "40.6556",
      "longitude": "29.2769"
    }
  },
  "areaServed": {
    "@type": "GeoCircle",
    "geoMidpoint": {
      "@type": "GeoCoordinates",
      "latitude": "40.6556",
      "longitude": "29.2769"
    },
    "geoRadius": "50000"
  }
}
```

---

### PHASE 7: Local SEO Tracking & Measurement (Ongoing)

#### 7.1. KPIs (Key Performance Indicators)

**Track Monthly:**

| Metric | Baseline | Target (3 months) | Target (6 months) |
|--------|----------|-------------------|-------------------|
| **Google "yalova erasmus" Rank** | N/A | #3 | #1 |
| **GBP Views** | 0 | 500/month | 1500/month |
| **GBP Actions (Calls, Website)** | 0 | 50/month | 150/month |
| **Local Pack Appearance** | 0% | 30% | 70% |
| **Organic Traffic (Yalova)** | N/A | 300/month | 800/month |
| **Review Count** | 0 | 15 | 40 |
| **Avg Rating** | N/A | 4.5+ | 4.7+ |
| **NAP Citations** | 2 | 15 | 30 |

---

#### 7.2. Tools for Tracking

1. **Google Business Profile Insights:**
   - Views
   - Search queries
   - Actions (calls, website visits, direction requests)

2. **Google Search Console:**
   - Filter by location (Yalova)
   - Track "yalova + keyword" queries
   - Monitor local pack appearances

3. **Google Analytics 4:**
   - Create segment: "Users from Yalova"
   - Track city-specific metrics
   - Goal: Form submissions from Yalova users

4. **Local Rank Tracker:**
   - BrightLocal (paid)
   - Whitespark (paid)
   - Or manual: VPN to Yalova IP + search

5. **Citation Tracker:**
   - Moz Local (paid)
   - Whitespark Citation Finder (paid)
   - Or manual: Spreadsheet NAP audit

---

## 📊 IMPLEMENTATION ROADMAP

### Week 1: Foundation
- [ ] Add full NAP (phone + address)
- [ ] Add geo coordinates to schema
- [ ] Update LocalBusiness schema (homepage)
- [ ] Create GBP listing

### Week 2: Service Pages
- [ ] Create yalova-dil-kurslari.html
- [ ] Add Service schema to Erasmus page
- [ ] Add Service schema to youth projects page
- [ ] Improve NAP consistency across site

### Week 3: Citations & GBP
- [ ] Verify GBP listing
- [ ] Add to Bing Places
- [ ] Add to Apple Maps
- [ ] Add to Yandex Business
- [ ] Complete Facebook Business page

### Week 4: Content & Backlinks
- [ ] Create success stories page
- [ ] Create partners page
- [ ] Create events calendar
- [ ] Reach out to Yalova Üniversitesi for partnership

### Week 5: Reviews & Monitoring
- [ ] Implement Review schema
- [ ] Set up review collection system
- [ ] Create review landing page
- [ ] Set up tracking dashboards

### Week 6-8: Optimization & Iteration
- [ ] Analyze GSC data
- [ ] Optimize underperforming pages
- [ ] A/B test CTA buttons
- [ ] Expand local content

---

## 🎯 EXPECTED RESULTS

### Month 1:
- ✅ GBP live and verified
- ✅ 10+ NAP citations
- ✅ 5+ reviews
- 📈 "yalova erasmus" → Top 10

### Month 3:
- ✅ 25+ NAP citations
- ✅ 20+ reviews (4.5+ rating)
- ✅ Local pack appearance 30%+
- 📈 "yalova erasmus" → Top 3
- 📈 500+ GBP views/month

### Month 6:
- ✅ 40+ reviews (4.7+ rating)
- ✅ Local pack dominant position
- 📈 "yalova erasmus" → #1
- 📈 1500+ GBP views/month
- 📈 800+ organic visits from Yalova
- 🎉 Recognized as #1 Yalova youth organization

---

## ⚠️ CRITICAL ACTIONS (This Week)

1. **Get Real NAP Information:**
   - Decide on office/working address
   - Get a phone number (mobile or VoIP)
   - Update everywhere

2. **Create Google Business Profile:**
   - https://www.google.com/business/
   - This is #1 priority for local SEO

3. **Add Google Maps to Website:**
   - Embed on homepage
   - Embed on contact page

4. **Update Schema on Homepage:**
   - Add telephone
   - Add geo coordinates
   - Add openingHours

---

## 💡 QUICK WINS (< 2 Hours)

1. **Add "Yalova" to All Page Titles:**
   - "Erasmus Başvuru" → "Yalova Erasmus Başvuru"
   - Better local keyword targeting

2. **Create Location-Specific H2:**
   - "Why Choose YouthTICK in Yalova?"
   - "Yalova'dan Erasmus Success Rate: 53%"

3. **Add Local Testimonials:**
   - Highlight "from Yalova" in testimonials
   - Use Person schema with homeLocation

4. **Footer Update:**
   - Add full address
   - Add phone (when ready)
   - Add "Serving Yalova since 2026"

---

## 🚀 LOCAL SEO CHECKLIST

### Technical:
- [ ] NAP consistent across all pages
- [ ] LocalBusiness schema with geo
- [ ] Service schema for each service
- [ ] Review schema for testimonials
- [ ] Google Maps embed
- [ ] Mobile-friendly (already ✅)

### Content:
- [ ] 6+ Yalova-specific pages (✅ exists)
- [ ] Location mentioned in H1/H2
- [ ] City name in meta descriptions
- [ ] Local keywords in content
- [ ] Success stories from Yalova

### Off-Page:
- [ ] Google Business Profile
- [ ] 10+ local citations
- [ ] 15+ reviews (4.5+ rating)
- [ ] Local backlinks (3+)
- [ ] Social media location tags

### Conversion:
- [ ] Click-to-call button
- [ ] Directions link
- [ ] Contact form (✅ exists)
- [ ] Clear CTA for Yalova users
- [ ] WhatsApp business integration

---

## 📞 NEXT STEPS

**Immediate (Today):**
1. Decide on NAP information
2. Create Google Business Profile
3. Update homepage schema

**This Week:**
1. Add Google Maps embed
2. Complete Bing/Apple/Yandex listings
3. Create yalova-dil-kurslari.html

**This Month:**
1. Collect first 10 reviews
2. Reach out to local partners
3. Start blog outreach for backlinks

---

**Questions?** Let me know if you need help implementing any of these steps!
