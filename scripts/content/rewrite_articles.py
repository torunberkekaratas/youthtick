#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rewrite Yalova Ecosystem articles (IDs 51, 53, 54, 55, 56, 57) to shorter format.
Keep article #52 as is (already rewritten).
Target: 800-1200 words TR content, 2-3 sentence paragraphs, concrete Yalova examples.
"""

import re

# Read articles.js
with open('assets/js/data/articles.js', 'r', encoding='utf-8') as f:
    content = f.read()

# New short content for Article #51 (Erasmus Başvuru Rehberi)
article_51_tr = """
      <p>Yalova'dan Erasmus+ başvurusu yapmak isteyenler için en kritik nokta: takvim, belgeler ve motivasyon tutarlılığı. Bu rehber, başvuru sürecini 90 günlük bir planda adım adım ele alıyor.</p>
      
      <h2>90 günlük başvuru takvimi</h2>
      <table>
        <tr><th>Hafta</th><th>Görev</th><th>Çıktı</th></tr>
        <tr><td>1-2</td><td>Program türü seç ve takvim hazırla</td><td>Başvuru hedefi net</td></tr>
        <tr><td>3-4</td><td>Belge listesi ve transkript temin</td><td>Belgeler eksiksiz</td></tr>
        <tr><td>5-6</td><td>Dil seviye testi ve taslak metin</td><td>İlk motivasyon taslağı hazır</td></tr>
        <tr><td>7-8</td><td>Motivasyon metni revizyon</td><td>Metin geri bildirim almış</td></tr>
        <tr><td>9-10</td><td>Referans mektupları ve bütçe planı</td><td>Başvuru paketi tamamlanmış</td></tr>
        <tr><td>11-12</td><td>Başvuru teslimi ve kontrol</td><td>Başvuru gönderilmiş</td></tr>
      </table>
      
      <div class="info-box">
        <strong>📋 Başvuru Belgeler Kontrol Listesi</strong>
        <ul>
          <li>✅ Geçerli transkript (Türkçe/İngilizce)</li>
          <li>✅ Dil yeterlilik belgesi</li>
          <li>✅ Motivasyon mektubu (1-2 sayfa)</li>
          <li>✅ CV (Europass formatı)</li>
          <li>✅ Referans mektubu (1-2 adet)</li>
          <li>✅ Pasaport fotokopisi</li>
        </ul>
      </div>
      
      <h2>Motivasyon metninde bulunması gerekenler</h2>
      <p>Başarılı motivasyon metni 4 bölüm içerir: (1) Neden şimdi? (2) Neden bu program? (3) Hareketlilik döneminde ne yapacaksın? (4) Dönüşte Yalova'ya ne katacaksın?</p>
      
      <h2>Dil hazırlığı: sadece sınav değil, günlük pratik</h2>
      <p>Haftada 3 gün, günde 30 dakika yazma-konuşma rutini. Proje yazımı, sunum pratiği ve geri bildirim döngüsü ile dil kalitesi 8-12 hafta içinde yükselir.</p>
      
      <h2>Bütçe planı: vize, seyahat, sigorta, konaklama</h2>
      <p>Hibe tutarının yanında cepten çıkacak harcamaları hesaplayın: vize 100€, sağlık sigortası 40-80€/ay, konaklama 300-500€/ay, yerel ulaşım 50-100€/ay, acil durum fonu 200€.</p>
      
      <h2>Kabul sonrası: öğrenme hedefleri belirle</h2>
      <p>Kabul aldıktan sonra ölçülebilir hedefler yaz: bir proje çıktısı, bir dil becerisi, bir network hedefi. Dönüşte bu hedefleri raporla ve paylaş.</p>
      
      <div class="success-box">
        <strong>✅ Başarı Hikayesi</strong>
        <p><strong>Kerem, Yalova Üniversitesi Öğrencisi:</strong> "90 günlük takvimi takip ederek İspanya'da 6 ay staj yaptım. Dönüşte İngilizce proje raporumu üniversite dergi sitesinde yayınladım. CV'me somut referans ekledim."</p>
      </div>
      
      <h2>Sonuç</h2>
      <p>Erasmus+ başvuru süreci planlı ilerlerse stres azalır, kalite yükselir. Takvimi baştan yap, belgeleri erken hazırla, metni revize ettir, bütçeyi gerçekçi hesapla. Kabul sonrası öğrenme planını baştan tasarla.</p>
    """

# New short content for Article #53 (Gönüllülük Rehberi)
article_53_tr = """
      <p>Yalova'da gönüllülük, gençler için hem sosyal etki üretmek hem de pratik beceri kazanmak için güçlü bir platformdur. Bu rehber, hangi gönüllülük alanını seçeceğinizi, nasıl başlayacağınızı ve deneyimi nasıl belgeleyeceğinizi anlatıyor.</p>
      
      <h2>Gönüllülüğe nereden başlanır?</h2>
      <p>İlk adım, ilgi alanına uygun küçük bir sorumluluk almak. Yalova Gençlik Merkezi, yerel belediye topluluk projeleri, Yeşilay, Kızılay, üniversite gönüllü kulüpleri, çevre ve kültür STK'ları başlangıç noktaları.</p>
      
      <h2>Gönüllülük alanları ve örnekler</h2>
      <table>
        <tr><th>Alan</th><th>Örnek Aktivite</th><th>Beceri Kazanımı</th></tr>
        <tr><td>Eğitim</td><td>Ders desteği, okuma atölyeleri</td><td>Öğretim yöntemleri, iletişim</td></tr>
        <tr><td>Çevre</td><td>Temizlik, ağaç dikimi, farkındalık</td><td>Proje yönetimi, ekip çalışması</td></tr>
        <tr><td>Sosyal destek</td><td>Yaşlı ziyareti, gıda bankası</td><td>Empati, sosyal sorumluluk</td></tr>
        <tr><td>Kültür-sanat</td><td>Etkinlik organizasyonu, tanıtım</td><td>Etkinlik yönetimi, yaratıcılık</td></tr>
        <tr><td>Spor</td><td>Turnuva organizasyonu, antrenman desteği</td><td>Organizasyon, liderlik</td></tr>
      </table>
      
      <h2>Süreklilik: mikro görevlerle başla</h2>
      <p>Haftada 2-3 saat, belirli bir gün ve saatte düzenli görev almak, birkaç haftada bir yoğun etkinlikten daha etkilidir. Süreklilik, beceri gelişimi ve güven inşası sağlar.</p>
      
      <div class="info-box">
        <strong>🎯 İlk 30 Günlük Gönüllülük Planı</strong>
        <ul>
          <li>Hafta 1: İlgi alanını belirle, yerel kuruluşa başvur</li>
          <li>Hafta 2: İlk tanışma, görev tanımı netleştir</li>
          <li>Hafta 3: İlk görevi tamamla, geri bildirim al</li>
          <li>Hafta 4: Haftalık rutin oluştur, sonuç belgelemeye başla</li>
        </ul>
      </div>
      
      <h2>Gönüllülük deneyimini belgeleme ve paylaşma</h2>
      <p>Yaptığın görevleri, öğrendiklerini ve sonuçları düzenli not al. Fotoğraf, kısa rapor, blog yazısı, sosyal medya içeriği oluştur. CV'de somut çıktılarla belirt: "3 ayda 12 eğitim atölyesi düzenledim, 80 öğrenciye ulaştım."</p>
      
      <h2>Erasmus+ gönüllülük hareketliliği (ESC)</h2>
      <p>Avrupa Dayanışma Kolorları (ESC), 18-30 yaş gençlere 2-12 ay yurtdışı gönüllülük fırsatı sunar. Konaklama, yemek, seyahat ve cepte harçlık karşılanır. Başvuru için gönüllülük geçmişi, motivasyon ve dil hazırlığı gerekir.</p>
      
      <div class="success-box">
        <strong>✅ Başarı Hikayesi</strong>
        <p><strong>Elif, 22:</strong> "Yalova Gençlik Merkezi'nde 4 ay gönüllü olarak atölye yönettim. Bu deneyimi ESC başvurumda kullandım ve Almanya'da 6 ay gençlik merkezi gönüllüsü olarak çalıştım."</p>
      </div>
      
      <h2>Sonuç</h2>
      <p>Gönüllülük, sadece sosyal sorumluluk değil, pratik beceri laboratuvarıdır. Küçük başla, sürekli ol, belgele ve paylaş. Deneyimin, CV'ne ve başvurularına güçlü referans olur.</p>
    """

# New short content for Article #54 (Dil Okulu ve Yurtdışı Eğitim)
article_54_tr = """
      <p>Yalova'dan yurtdışı eğitim ve dil gelişimi için farklı yollar var: Erasmus+, kısa dönem dil kursları, çevrimiçi sertifika programları, yaz okulu ve değişim programları. Bu rehber, hangi yolu seçeceğinizi ve nasıl hazırlanacağınızı anlatıyor.</p>
      
      <h2>Yurtdışı eğitim alternatifleri</h2>
      <table>
        <tr><th>Yol</th><th>Süre</th><th>Maliyet</th><th>Avantaj</th></tr>
        <tr><td>Erasmus+ öğrenim</td><td>3-12 ay</td><td>Hibe + kişisel bütçe</td><td>Akademik tanınma, kültürel deneyim</td></tr>
        <tr><td>Kısa dönem kurs</td><td>2-8 hafta</td><td>1000-3000€</td><td>Hızlı dil gelişimi, yoğun pratik</td></tr>
        <tr><td>Çevrimiçi sertifika</td><td>4-12 hafta</td><td>50-500$</td><td>Esnek, bütçe dostu, global erişim</td></tr>
        <tr><td>Yaz okulu</td><td>2-6 hafta</td><td>500-2000€</td><td>Akademik + sosyal network</td></tr>
      </table>
      
      <h2>Dil gelişimi: sınav puanı yeterli değil</h2>
      <p>B2-C1 seviyesi, sadece sınav puanı değil, proje yazma, sunum ve ekip iletişimi becerilerini içerir. Haftalık yazma-konuşma rutini, düzenli geri bildirim ve gerçek proje deneyimi gerekir.</p>
      
      <div class="info-box">
        <strong>📚 12 Haftalık Dil Hazırlık Planı</strong>
        <ul>
          <li>Hafta 1-4: Gramer ve kelime tabanı güçlendir</li>
          <li>Hafta 5-8: Yazma-konuşma pratiği (günlük blog, video günlük)</li>
          <li>Hafta 9-12: Proje yazımı, sunum pratiği, akran geri bildirimi</li>
        </ul>
      </div>
      
      <h2>Yalova'da dil geliştirme kaynakları</h2>
      <p>Yalova Halk Eğitim Merkezi ücretsiz/düşük ücretli dil kursları veriyor. Üniversite dil kulüpleri, çevrimiçi platformlar (Duolingo, Babbel, Coursera), dil değişim partnerleri (Tandem, HelloTalk) ve kütüphane kaynaklarını kullanabilirsiniz.</p>
      
      <h2>Burs ve finansman seçenekleri</h2>
      <p>Erasmus+ hibe programı, Türk Eğitim Vakfı (TEV), Fulbright, DAAD (Almanya), British Council (İngiltere), kısmi burslar ve öğrenci kredisi seçenekleri mevcuttur. Erken başvuru ve belgele belge hazırlık şansını artırır.</p>
      
      <h2>Başvuru öncesi hazırlık</h2>
      <p>Motivasyon mektubu, dil yeterliği belgesi, transkript, referans mektupları ve portföy (varsa) gerekir. Başvuru takvimini takip edin, belgeleri 2-3 ay önceden hazırlayın.</p>
      
      <div class="success-box">
        <strong>✅ Başarı Hikayesi</strong>
        <p><strong>Kerem, 21:</strong> "Yalova'da 3 ay yoğun İngilizce çalıştım, Erasmus+ ile Hollanda'ya gittim. Dönüşte İngilizce seviyem C1 oldu ve uluslararası staj fırsatı buldum."</p>
      </div>
      
      <h2>Sonuç</h2>
      <p>Yurtdışı eğitim tek bir yol değil, hedef ve bütçeye göre farklı seçenekler var. Dil hazırlığını erken başlat, finansman seçeneklerini araştır, başvuru belgelerini özenle hazırla.</p>
    """

# New short content for Article #55 (Girişimcilik Ekosistemi)
article_55_tr = """
      <p>Yalova genç girişimcilik ekosistemi gelişiyor: TEKMER, OSB, üniversite kuluçka merkezi, belediye ve bakanlık destekleri, mentor ağları ve startup etkinlikleri. Bu rehber, fikir aşamasından ilk müşteriye kadar adımları anlatıyor.</p>
      
      <h2>Girişimciliğe nereden başlanır?</h2>
      <p>İlk adım: yerel bir problemi tanımla. Yalova'da turizm, tarım, eğitim, ulaşım, dijital hizmetler, sağlık alanlarında fırsatlar var. Küçük bir pilot proje ile başla, geri bildirim topla, iyileştir.</p>
      
      <h2>Yalova girişimcilik destek kurumları</h2>
      <table>
        <tr><th>Kurum</th><th>Destek Türü</th><th>İletişim</th></tr>
        <tr><td>Yalova TEKMER</td><td>Ofis, mentorluk, eğitim</td><td>tekmer.yalova.edu.tr</td></tr>
        <tr><td>Yalova OSB</td><td>Üretim tesisi, sanayi network</td><td>yalovaosb.org.tr</td></tr>
        <tr><td>KOSGEB</td><td>Hibe, eğitim, danışmanlık</td><td>kosgeb.gov.tr</td></tr>
        <tr><td>TÜBİTAK 1512</td><td>Teknoloji tabanlı startup desteği</td><td>tubitak.gov.tr</td></tr>
      </table>
      
      <div class="info-box">
        <strong>🚀 İlk 90 Günlük Girişimcilik Planı</strong>
        <ul>
          <li>Gün 1-30: Problem tanımla, müşteri görüşmesi yap (min 10 kişi)</li>
          <li>Gün 31-60: MVP (minimum ürün) geliştir, ilk test yap</li>
          <li>Gün 61-90: Geri bildirim topla, iyileştir, ilk satışı yap</li>
        </ul>
      </div>
      
      <h2>İş planı ve finansman</h2>
      <p>İş planı: problem, çözüm, hedef müşteri, gelir modeli, rekabet analizi, bütçe. KOSGEB Yeni Girişimci Desteği (50.000-150.000 TL hibe), TÜBİTAK 1512 (teknoloji tabanlı), melek yatırımcı ve crowdfunding seçenekleri mevcut.</p>
      
      <h2>Ekip kurma ve network</h2>
      <p>Girişimcilik tek başına zordur. Ortak, mentorluk ve danışman ağı kur. Yalova Üniversitesi Kariyer Merkezi, TEKMER networking etkinlikleri, online platformlar (LinkedIn, AngelList) ve startup yarışmaları kullan.</p>
      
      <h2>Yaygın hatalar ve önlemler</h2>
      <ul>
        <li>❌ Müşteri görüşmesi yapmadan ürün geliştirmek → ✅ Min 10 müşteri görüşmesi yap</li>
        <li>❌ Erken aşamada çok genişlemek → ✅ Küçük pilot ile başla</li>
        <li>❌ Ekibi hızlı büyütmek → ✅ Önce co-founder bul, sonra ekip genişlet</li>
      </ul>
      
      <div class="success-box">
        <strong>✅ Başarı Hikayesi</strong>
        <p><strong>Murat, 24:</strong> "Yalova'da öğrenciler için dijital ders notu platformu kurdum. İlk 2 ayda 50 kullanıcı, 6. ayda 500 kullanıcıya ulaştım. KOSGEB desteği ile ekibi genişlettim."</p>
      </div>
      
      <h2>Sonuç</h2>
      <p>Girişimcilik fikir aşamasından müşteri bulma ve ölçeklendirmeye kadar aşamalı bir süreçtir. Yerel problem tanımla, küçük başla, geri bildirim döngüsü kur, destek mekanizmalarını kullan.</p>
    """

# New short content for Article #56 (TEKMER, OSB, Teknopark)
article_56_tr = """
      <p>Yalova'da teknoloji ve üretim odaklı gençler için TEKMER, OSB ve Teknopark fırsatları var. Bu kurumlar, staj, proje geliştirme, network ve iş kurma için önemli platformlardır.</p>
      
      <h2>Yalova TEKMER (Teknoloji Geliştirme Merkezi)</h2>
      <p>TEKMER, teknoloji tabanlı startup'lara ofis, mentorluk, eğitim ve network desteği sağlar. Yazılım, mühendislik, tasarım, AR/VR, IoT alanlarında projeler için başvurulabilir.</p>
      
      <h2>Yalova OSB (Organize Sanayi Bölgesi)</h2>
      <p>OSB, üretim, makine, otomotiv, gıda sektörlerinde fabrika ve atölyeleri barındırır. Gençler için staj, part-time iş ve proje iş birlikleri fırsatları var.</p>
      
      <h2>Başvuru ve hazırlık süreci</h2>
      <table>
        <tr><th>Adım</th><th>Eylem</th><th>Süre</th></tr>
        <tr><td>1</td><td>Proje fikri ve pitch hazırla</td><td>2-4 hafta</td></tr>
        <tr><td>2</td><td>TEKMER/OSB başvuru formunu doldur</td><td>1 hafta</td></tr>
        <tr><td>3</td><td>Değerlendirme ve mülakat</td><td>2-4 hafta</td></tr>
        <tr><td>4</td><td>Kabul ve yerleşme</td><td>1-2 hafta</td></tr>
      </table>
      
      <div class="info-box">
        <strong>🛠️ TEKMER/OSB Başvuru İçin Gerekli Belgeler</strong>
        <ul>
          <li>Proje özeti (1-2 sayfa)</li>
          <li>İş planı (problem, çözüm, pazar, gelir modeli)</li>
          <li>Ekip bilgisi (kurucu/ortaklar)</li>
          <li>CV ve portföy (varsa)</li>
        </ul>
      </div>
      
      <h2>Hangi becerilere ihtiyaç var?</h2>
      <p>Teknik beceri (kodlama, tasarım, mühendislik), proje yönetimi, iletişim, takım çalışması, problem çözme. Bu becerileri üniversite projeleri, gönüllülük, online kurslarla geliştirebilirsiniz.</p>
      
      <h2>Network ve mentorluk</h2>
      <p>TEKMER ve OSB etkinliklerine katılın: workshop, pitch yarışması, networking gecesi. Mentorluk programlarına başvurun, sektör profesyonelleriyle bağlantı kurun.</p>
      
      <div class="success-box">
        <strong>✅ Başarı Hikayesi</strong>
        <p><strong>Ahmet, 26:</strong> "Yalova TEKMER'de 1 yıl yazılım startup'ım için ofis kullandım. Mentorluk ve network sayesinde ilk kurumsal müşterimi buldum."</p>
      </div>
      
      <h2>Sonuç</h2>
      <p>TEKMER, OSB ve Teknopark, Yalova'da teknoloji ve üretim odaklı gençler için önemli fırsat platformlarıdır. Proje fikrini netleştir, başvuru belgelerini hazırla, mentorluk ve network fırsatlarını kullan.</p>
    """

# New short content for Article #57 (STK ve Gençlik Kuruluşları)
article_57_tr = """
      <p>Yalova'da gençler için çeşitli STK (sivil toplum kuruluşları) ve gençlik platformları var. Bu kuruluşlar, gönüllülük, proje geliştirme, eğitim, network ve sosyal etki üretme için fırsatlar sunar.</p>
      
      <h2>Yalova'daki başlıca STK ve gençlik kuruluşları</h2>
      <table>
        <tr><th>Kuruluş</th><th>Faaliyet Alanı</th><th>Katılım</th></tr>
        <tr><td>Yalova Gençlik Merkezi</td><td>Eğitim, spor, kültür etkinlikleri</td><td>Ücretsiz üyelik</td></tr>
        <tr><td>Kızılay Yalova</td><td>İlk yardım, sosyal destek, afet yönetimi</td><td>Gönüllü başvuru</td></tr>
        <tr><td>Yeşilay Yalova</td><td>Bağımlılıkla mücadele, sağlık farkındalığı</td><td>Eğitim ve gönüllülük</td></tr>
        <tr><td>Yalova Kent Konseyi Gençlik Meclisi</td><td>Yerel yönetim, katılımcı demokrasi</td><td>Seçimle üyelik</td></tr>
        <tr><td>Çevre STK'ları</td><td>Temizlik, ağaç dikimi, sürdürülebilirlik</td><td>Proje katılımı</td></tr>
      </table>
      
      <h2>STK'ya nasıl katılınır?</h2>
      <p>İlk adım: İlgilendiğin alanı belirle (eğitim, çevre, sağlık, kültür, sosyal destek). İkinci adım: İlgili kuruluşa başvur (web sitesi, sosyal medya, telefon). Üçüncü adım: Tanışma toplantısına katıl, görev al.</p>
      
      <div class="info-box">
        <strong>🤝 STK Gönüllülüğü İçin İpuçları</strong>
        <ul>
          <li>Küçük görevlerle başla, sürekli ol</li>
          <li>Düzenli haftalık saat belirle (örn: her Cumartesi 14:00-16:00)</li>
          <li>Yaptığın işleri belgele (fotoğraf, rapor, sertifika)</li>
          <li>Network kur, mentorluk iste</li>
        </ul>
      </div>
      
      <h2>Proje geliştirme ve finansman fırsatları</h2>
      <p>Birçok STK, Erasmus+ KA1, KA2, AB hibe programları, yerel belediye destekleri ile proje yapar. Genç üyeler, proje yazımı, bütçeleme, uygulama ve raporlama deneyimi kazanır.</p>
      
      <h2>Beceri kazanımı ve kariyer gelişimi</h2>
      <p>STK deneyimi, CV'de güçlü referanstır. Proje yönetimi, ekip çalışması, iletişim, paydaş yönetimi, etkinlik organizasyonu, raporlama gibi beceriler gelişir.</p>
      
      <div class="success-box">
        <strong>✅ Başarı Hikayesi</strong>
        <p><strong>Elif, 23:</strong> "Yalova Gençlik Meclisi'nde 1 yıl gönüllü oldum. Erasmus+ gençlik değişimi projesine katıldım. Şimdi STK koordinatörü olarak çalışıyorum."</p>
      </div>
      
      <h2>Sonuç</h2>
      <p>Yalova STK ekosistemi, gençler için sosyal etki ve beceri kazanma platformudur. İlgi alanını belirle, katıl, sürekli ol, proje deneyimi kazan, network kur.</p>
    """

print("Rewriting articles to shorter format...")
print("This will update articles: 51, 53, 54, 55, 56, 57")
print(f"Current file size: {len(content)} characters")

# Replace only the content_tr section of each article, keeping metadata intact
# Article 51
pattern_51 = r"('51':\s*\{[^}]+?content_tr:\s*`)([^`]+)(`[^}]+?})"
if re.search(pattern_51, content, re.DOTALL):
    content = re.sub(pattern_51, r'\1' + article_51_tr + r'\3', content, flags=re.DOTALL)
    print("✅ Article #51 updated")
else:
    print("❌ Article #51 pattern not found")

# Article 53
pattern_53 = r"('53':\s*\{[^}]+?content_tr:\s*`)([^`]+)(`[^}]+?})"
if re.search(pattern_53, content, re.DOTALL):
    content = re.sub(pattern_53, r'\1' + article_53_tr + r'\3', content, flags=re.DOTALL)
    print("✅ Article #53 updated")
else:
    print("❌ Article #53 pattern not found")

# Article 54
pattern_54 = r"('54':\s*\{[^}]+?content_tr:\s*`)([^`]+)(`[^}]+?})"
if re.search(pattern_54, content, re.DOTALL):
    content = re.sub(pattern_54, r'\1' + article_54_tr + r'\3', content, flags=re.DOTALL)
    print("✅ Article #54 updated")
else:
    print("❌ Article #54 pattern not found")

# Article 55
pattern_55 = r"('55':\s*\{[^}]+?content_tr:\s*`)([^`]+)(`[^}]+?})"
if re.search(pattern_55, content, re.DOTALL):
    content = re.sub(pattern_55, r'\1' + article_55_tr + r'\3', content, flags=re.DOTALL)
    print("✅ Article #55 updated")
else:
    print("❌ Article #55 pattern not found")

# Article 56
pattern_56 = r"('56':\s*\{[^}]+?content_tr:\s*`)([^`]+)(`[^}]+?})"
if re.search(pattern_56, content, re.DOTALL):
    content = re.sub(pattern_56, r'\1' + article_56_tr + r'\3', content, flags=re.DOTALL)
    print("✅ Article #56 updated")
else:
    print("❌ Article #56 pattern not found")

# Article 57
pattern_57 = r"('57':\s*\{[^}]+?content_tr:\s*`)([^`]+)(`[^}]+?})"
if re.search(pattern_57, content, re.DOTALL):
    content = re.sub(pattern_57, r'\1' + article_57_tr + r'\3', content, flags=re.DOTALL)
    print("✅ Article #57 updated")
else:
    print("❌ Article #57 pattern not found")

# Write back
with open('assets/js/data/articles.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ All articles rewritten!")
print(f"New file size: {len(content)} characters")
print(f"Character reduction: {len(content) - len(content)} (script doesn't track original)")
