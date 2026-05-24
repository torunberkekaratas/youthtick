#!/usr/bin/env python3
"""Add TR + DE translations for articles 36-46."""
import re, sys

path = "assets/js/data/articles.js"
with open(path, encoding="utf-8") as f:
    content = f.read()

translations = {
    '36': {
        'title_tr': "Net Sıfır ve Gençlik: Avrupa'nın 2050 İklim Yol Haritasını Anlamak",
        'title_de': "Netto-Null und Jugend: Europas Klimafahrplan 2050 verstehen",
        'content_tr': """
      <p>Avrupa Birliği'nin 2050 yılına kadar iklim tarafsızlığına — net sıfır sera gazı emisyonlarına — ulaşma taahhüdü, Avrupa tarihindeki en iddialı uzun vadeli politika hedefidir. Bu yol haritasının kapsadığı dönemin büyük bölümünde yaşayacak olan gençler için bunun pratikte ne anlama geldiğini anlamak isteğe bağlı arka plan bilgisi değildir. Bu bir vatandaşlık okuryazarlığıdır.</p>
      <h2>Net Sıfır Gerçekte Ne Anlama Geliyor?</h2>
      <p>Net sıfır sıfır emisyon anlamına gelmez. Atmosfere salınan sera gazı emisyonlarının eşit miktarda atmosferden uzaklaştırılmasıyla dengelenmesi anlamına gelir — ormanlar ve topraklar gibi doğal karbon yuvaları veya teknolojik karbon yakalama yoluyla. AB'nin hedefi bu dengeye 2050'ye kadar ulaşmaktır; ara kilometre taşı olarak 1990 seviyelerine kıyasla 2030'a kadar emisyonları en az %55 azaltmak öngörülmektedir.</p>
      <h2>Sektör Sektör Yol Haritası</h2>
      <p>Net sıfır yolu farklı sektörleri farklı biçimlerde etkiler. Enerji sektörü için 2035'e kadar elektrikte fosil yakıt elektrik üretiminden yenilenebilir enerjiye — ağırlıklı olarak güneş ve rüzgar — geçiş anlamına gelir. Ulaşım için 2035'e kadar yeni benzinli ve dizel araç satışlarının sona ermesi anlamına gelir. Binalar için derin yenileme çalışmaları — AB mevcut bina stoğunun %75'inin yenilenmesi gerektiğini tahmin etmektedir.</p>
      <blockquote>Net sıfır öncelikle bir teknoloji sorunu değildir. Teknolojiler mevcuttur. Öncelikle bir siyasi ekonomi sorunudur: fosil yakıt ekonomisine bağımlı işçiler, topluluklar ve endüstriler için yarattığı bozulmayı yönetirken değişimi yeterince hızlı nasıl yaparsınız?</blockquote>
      <h2>Adil Geçiş: Maliyeti Kim Üstleniyor?</h2>
      <p>Net sıfır yol haritasının siyasi açıdan en hassas boyutu dağılım sorusudur: yeşil geçişten kim yararlanıyor ve maliyeti kim üstleniyor? Kömür madenciliğine, fosil yakıt rafinerisine veya karbon yoğun imalata bağımlı topluluklar önemli ekonomik aksaklıklarla karşı karşıyadır.</p>
      <h2>Gençlerin Yapabilecekleri</h2>
      <p>Gençlerin net sıfır geçişindeki rolü yalnızca gelecekteki yararlanıcılar olarak değil — onu gerçekleştirmede aktif katılımcılar olarak da söz konusudur. Bu şunları kapsar: geçiş ekonomisinde istihdam edilebilirlik için yeşil beceriler geliştirme; geçişin nasıl yönetileceğini belirleyen demokratik süreçlere katılma; politikacıları ve şirketleri taahhütleri konusunda sorumlu tutma.</p>
    """,
        'content_de': """
      <p>Das Bekenntnis der Europäischen Union zur Klimaneutralität — Netto-Null-Treibhausgasemissionen — bis 2050 ist das ehrgeizigste langfristige Politikziel in der europäischen Geschichte. Für junge Menschen, die den größten Teil ihres Lebens in dem von diesem Fahrplan abgedeckten Zeitraum verbringen werden, ist das Verständnis, was das in der Praxis bedeutet, kein optionales Hintergrundwissen. Es ist Staatsbürgerkunde.</p>
      <h2>Was Netto-Null wirklich bedeutet</h2>
      <p>Netto-Null bedeutet nicht null Emissionen. Es bedeutet, dass Treibhausgasemissionen, die in die Atmosphäre freigesetzt werden, durch eine gleiche Menge ausgeglichen werden, die daraus entfernt wird — entweder durch natürliche Kohlenstoffsenken wie Wälder und Böden oder durch technologische Kohlenstoffabscheidung. Das EU-Zwischenziel lautet: bis 2030 Emissionen um mindestens 55% gegenüber 1990 reduzieren.</p>
      <h2>Der Fahrplan: Sektor für Sektor</h2>
      <p>Für den Energiesektor bedeutet es den Wechsel von fossiler Stromerzeugung zu erneuerbaren Energien bis 2035. Für den Transport bedeutet es das Ende des Verkaufs neuer Benzin- und Dieselfahrzeuge bis 2035. Für Gebäude bedeutet es tiefe Sanierungen — die EU schätzt, dass 75% des bestehenden Gebäudebestands renoviert werden müssen.</p>
      <blockquote>Netto-Null ist nicht primär eine Technologieherausforderung. Die Technologien existieren. Es ist primär eine politisch-ökonomische Herausforderung: Wie macht man den Wandel schnell genug, während man die Störungen für Arbeitnehmer, Gemeinschaften und Industrien managt, die von der fossilen Brennstoffwirtschaft abhängen?</blockquote>
      <h2>Gerechter Übergang: Wer trägt die Kosten?</h2>
      <p>Die politisch sensibelste Dimension ist die Frage der Verteilung: Wer profitiert von der grünen Transition, und wer trägt die Kosten? Gemeinschaften, die vom Kohlebergbau abhängen, stehen vor erheblichen wirtschaftlichen Störungen.</p>
      <h2>Was junge Menschen tun können</h2>
      <p>Die Rolle junger Menschen ist nicht nur als zukünftige Begünstigte — sondern als aktive Teilnehmer daran, es Wirklichkeit werden zu lassen: grüne Kompetenzen entwickeln, demokratische Prozesse nutzen, Politiker und Unternehmen zur Rechenschaft ziehen.</p>
    """
    },
    '37': {
        'title_tr': 'Biyoçeşitlilik Kaybı ve Gençlik Çalışması: Doğanın Programlarınızda Neden Yeri Var',
        'title_de': 'Biodiversitätsverlust und Jugendarbeit: Warum Natur in Ihre Programme gehört',
        'content_tr': """
      <p>İklim değişikliği kamuoyunun çevre söylemini domine ediyor — ve buna iyi bir nedeni var. Ancak biyoçeşitlilik krizi de aynı ölçüde acil, aynı ölçüde insan kaynaklı ve bazı açılardan insan refahı için daha da hemen tehdit edicidir. Gençlik çalışması bu konuya yavaş eğilmiştir. Bu düzeltilmeye değer bir hatadır.</p>
      <h2>Krizin Boyutu</h2>
      <p>IPBES'in 2019 tarihli Küresel Değerlendirmesi — türünün en kapsamlı incelemesi — yaklaşık bir milyon hayvan ve bitki türünün insan tarihindeki herhangi bir önceki noktadan daha fazla nesil tükenme tehdidiyle karşı karşıya olduğunu bulmuştur. WWF'nin Yaşayan Gezegen Endeksi'ne göre küresel yaban hayatı popülasyonları 1970'den bu yana ortalama %69 azalmıştır.</p>
      <p>Bunlar yalnızca ekolojik istatistikler değildir. Biyoçeşitlilik, insan medeniyetinin bağımlı olduğu ekosistem hizmetlerinin temelini oluşturur: gıda ürünlerinin tozlaşması, tatlısu arıtma, sel düzenleme, iklim düzenleme, toprak oluşumu, hastalık kontrolü.</p>
      <blockquote>Bilmediğiniz bir şeye önem veremezsiniz. Avrupalı şehirlerdeki gençlerin büyük çoğunluğu doğal sistemlerle neredeyse hiç temas kurmamıştır. Bu teması yaratan gençlik çalışması — kısa süreliğine de olsa, yerel düzeyde de olsa — çok daha büyük bir şeye dönüşebilecek tohumlar eker.</blockquote>
      <h2>Biyoçeşitliği Entegre Etmenin Pratik Yolları</h2>
      <ul>
        <li><strong>Kentsel doğa keşfi</strong>: kentsel yeşil alanlarda rehberli yürüyüşler, vatandaş bilim faaliyetleri ve biyoçeşitlilik araştırmaları</li>
        <li><strong>Doğa tabanlı kolaylaştırma</strong>: atölyeleri açık havada yürütme, doğal malzemeler kullanma</li>
        <li><strong>iNaturalist ve vatandaş bilimi</strong>: gençlerin yerel türler hakkında gerçek bilimsel verilere katkıda bulunmasını sağlayan uygulamalar</li>
        <li><strong>Gıda sistemleriyle bağlantı</strong>: yiyeceğin nereden geldiğini, nasıl üretildiğini keşfetmek</li>
        <li><strong>Politika okuryazarlığı</strong>: gençlerin AB Biyoçeşitlilik Stratejisini ve Küresel Biyoçeşitlilik Çerçevesini anlamalarına yardımcı olmak</li>
      </ul>
      <h2>Derin Gerekçe</h2>
      <p>Pratik argümanların ötesinde daha derin bir gerekçe var. Doğayla temas, gençlerin ruh sağlığı, dikkat ve kendilerinden daha büyük bir şeye ait olma hissi üzerinde iyi belgelenmiş faydaları vardır. Doğa yalnızca bir çevre meselesi değildir. Bir refah meselesidir. Ve refah gençlik çalışmasının amacıdır.</p>
    """,
        'content_de': """
      <p>Der Klimawandel dominiert den öffentlichen Umweltdiskurs — und das aus gutem Grund. Aber die Biodiversitätskrise ist ebenso dringend, ebenso durch Menschen verursacht und in mancher Hinsicht unmittelbarer bedrohlich für das menschliche Wohlbefinden. Die Jugendarbeit war langsam damit, sich damit zu befassen. Das ist ein Fehler, den es wert ist, zu korrigieren.</p>
      <h2>Das Ausmaß der Krise</h2>
      <p>Die IPBES-Globalbewertung von 2019 stellte fest, dass rund eine Million Tier- und Pflanzenarten aktuell vom Aussterben bedroht sind, mehr als je zuvor in der Menschheitsgeschichte. Globale Wildtierpopulationen sind seit 1970 um durchschnittlich 69% zurückgegangen.</p>
      <blockquote>Man kann sich nicht um etwas kümmern, das man nicht kennt. Die meisten jungen Menschen in europäischen Städten haben fast keinen Kontakt mit natürlichen Systemen. Jugendarbeit, die diesen Kontakt schafft — auch kurz, auch lokal — pflanzt Samen, die zu etwas viel Größerem heranwachsen können.</blockquote>
      <h2>Praktische Wege zur Integration von Biodiversität</h2>
      <ul>
        <li><strong>Städtische Naturerkundung</strong>: geführte Spaziergänge und Biodiversitätserhebungen in städtischen Grünflächen</li>
        <li><strong>Naturbasierte Moderation</strong>: Workshops im Freien durchführen</li>
        <li><strong>iNaturalist und Bürgerwissenschaft</strong>: Apps, mit denen junge Menschen zu echten wissenschaftlichen Daten über lokale Arten beitragen</li>
        <li><strong>Verbindung zu Lebensmittelsystemen</strong>: erkunden, woher Lebensmittel kommen und wie sie produziert werden</li>
        <li><strong>Politikkompetenz</strong>: jungen Menschen helfen, die EU-Biodiversitätsstrategie zu verstehen</li>
      </ul>
      <h2>Der tiefere Fall</h2>
      <p>Der Kontakt mit der Natur hat gut dokumentierte Vorteile für die psychische Gesundheit junger Menschen. Natur ist nicht nur ein Umweltthema. Es ist ein Wohlbefindenthema. Und Wohlbefinden ist das Ziel der Jugendarbeit.</p>
    """
    },
    '38': {
        'title_tr': "Avrupalı Olmak Ne Anlama Geliyor? 2025'te Gençlerin Yanıtları",
        'title_de': "Was bedeutet es, Europäer zu sein? Antworten junger Menschen im Jahr 2025",
        'content_tr': """
      <p>Her nesil Avrupa'ya ait olmanın ne anlama geldiğini yeniden tanımlar. 2025'teki gençler için — kıtanın büyük bölümünde ortak para birimi olmayan bir Avrupa'yı hiç bilmemiş, Erasmus+ olmayan bir Avrupa'yı tanımamış ve aynı anda dijital küresel ve yoğun biçimde yerel kimlikler arasında büyümüş nesil — bu sorunun yanıtları siyasi tartışmanın genellikle izin verdiğinden daha nüanslıdır ve daha ilginçtir.</p>
      <h2>Anketlerin Söyledikleri</h2>
      <p>Avrupa Komisyonu'nun Eurobarometresi tutarlı biçimde genç insanların (15-30) daha yaşlı yaş gruplarından daha yüksek Avrupa kimliği düzeyleri bildirdiğini ortaya koyar. Genç Avrupalıların yaklaşık %70'i ulusal kimliklerinin yanı sıra "Avrupalı" hissettiğini bildiriyor — bunun yerine değil, buna ek olarak. Çift veya çoklu aidiyetin hissi karakteristiktir.</p>
      <blockquote>İyi bağlantılı kentsel bir aileden gelen, Erasmus+ değişimi yapmış, üç ülkede çalışmış ve Avrupa genelinde arkadaşları olan genç, Avrupa kimliğini, niteliksiz ve uluslararası bağlantısız küçük bir kasabadaki gençten çok farklı biçimde deneyimler. Her ikisi de eşit ölçüde Avrupalıdır. Bunun anlamı büyük farklılıklar gösterir.</blockquote>
      <h2>Türkiye'nin Avrupa Kimliği Sorusundaki Konumu</h2>
      <p>Derin Avrupa bağları, AB ile devam eden kurumsal ilişkiler ve karmaşık jeopolitik bir konuma sahip Türkiye'deki gençler için Avrupa kimliği sorusu özellikle önem taşır. Araştırmalar tutarlı biçimde pek çok Türk gencinin kültürel açıdan Avrupa'ya bağlı hissettiğini göstermektedir — paylaşılan değerler, eğitim deneyimi ve aile bağları aracılığıyla — bununla birlikte durdurulan üyelik süreci nedeniyle resmi Avrupa aidiyetinden dışlandığını hissettiklerini ortaya koymaktadır.</p>
      <h2>Gençlik Çalışmasının Sunabilecekleri</h2>
      <p>Gençlik değişimleri ve kültürlerarası programlar, gençlerin Avrupa kimliğinin onlar için pratikte ne anlama geldiğini keşfedebileceği nadir alanlardan birini yaratır — soyut bir kavram olarak değil, gerçek ilişkiler, paylaşılan deneyimler ve dürüst diyalog aracılığıyla.</p>
    """,
        'content_de': """
      <p>Jede Generation definiert neu, was es bedeutet, Europa anzugehören. Für junge Menschen im Jahr 2025 — die erste Generation, die nie ein Europa ohne gemeinsame Währung kannte, nie ohne Erasmus+ — sind die Antworten nuancierter und interessanter, als es die politische Debatte typischerweise zulässt.</p>
      <h2>Was die Umfragen sagen</h2>
      <p>Das Eurobarometer der Europäischen Kommission zeigt konsistent, dass junge Menschen (15–30) höhere Werte europäischer Identität berichten als ältere Altersgruppen. Etwa 70% der jungen Europäer berichten, sich „europäisch" zu fühlen — neben ihrer nationalen Identität, nicht statt ihr.</p>
      <blockquote>Der junge Mensch aus einer gut vernetzten städtischen Familie, der einen Erasmus+-Austausch gemacht hat, in drei Ländern gearbeitet hat und Freunde in ganz Europa hat, erlebt europäische Identität ganz anders als der junge Mensch in einer kleinen Stadt ohne Qualifikationen und ohne internationale Verbindungen. Beide sind gleichermaßen europäisch. Die Bedeutung davon unterscheidet sich enorm.</blockquote>
      <h2>Die Position der Türkei in der europäischen Identitätsfrage</h2>
      <p>Für junge Menschen in der Türkei — einem Land mit tiefen europäischen Bindungen — trägt die Frage der europäischen Identität besonderes Gewicht. Forschungen zeigen konsistent, dass viele junge Türken sich kulturell mit Europa verbunden fühlen — durch gemeinsame Werte, Bildungserfahrung und Familienverbindungen — während sie sich durch den ins Stocken geratenen Beitrittsprozess von der formellen europäischen Zugehörigkeit ausgeschlossen fühlen.</p>
      <h2>Was Jugendarbeit anbieten kann</h2>
      <p>Jugendaustausche und interkulturelle Programme schaffen einen der wenigen Räume, in denen junge Menschen erkunden können, was europäische Identität für sie in der Praxis bedeutet — nicht als abstraktes Konzept, sondern durch echte Beziehungen und ehrlichen Dialog.</p>
    """
    },
    '39': {
        'title_tr': 'Gençlik Çalışmasında Dini Çeşitlilikle Başa Çıkmak: Pratik Rehber',
        'title_de': 'Religiöse Vielfalt in der Jugendarbeit navigieren: Ein praktischer Leitfaden',
        'content_tr': """
      <p>Din, gençlerin önemli bir bölümünün hayatını — değerlerini, pratiklerini, topluluk hissini ve dünya anlayışlarını — şekillendirir. Yine de Avrupa'nın büyük bölümündeki gençlik çalışması dini, dikkatle kaçınılması gereken bir konu olarak ele alır: çok hassas, çok bölücü, çok fazla çatışmaya yol açabilecek. Bu kaçınma anlaşılabilirdir. Aynı zamanda alanın bir başarısızlığıdır.</p>
      <h2>Gençlik Çalışması Dinden Neden Kaçınıyor?</h2>
      <p>Kaçınma kısmen tarihidir. Avrupa gençlik çalışması büyük ölçüde dini özel bir mesele olarak konumlandıran laik siyasi geleneklerde gelişti. Aynı zamanda kısmen pragmatiktir: din karma gruplarda çatışma yaratabilir.</p>
      <h2>Kaçınmanın Bedeli</h2>
      <p>İnancı kimliklerinin merkezinde deneyimleyen gençler için — ve araştırmalar bunun Avrupa'daki gençlerin önemli bir azınlığı için geçerli olduğunu göstermektedir, özellikle göçmen kökenli topluluklarda — kaçınma açık bir mesaj gönderir: kim olduğunuzun bu önemli parçası burada hoş karşılanmıyor.</p>
      <blockquote>Birlikte çalıştığınız gençlerin büyük çoğunluğu için en merkezi deneyim boyutunu sistematik biçimde dışlıyorsanız kültürlerarası diyalog pratiği yaptığınızı iddia edemezsiniz. Dini kimlik kültürel kimliktir. İkisi ayrılamaz.</blockquote>
      <h2>Pratik Yaklaşımlar</h2>
      <ul>
        <li><strong>Diyet konaklama</strong>: helal, koşer ve vejetaryen seçenekler içeren ikram</li>
        <li><strong>Program esnekliği</strong>: programları planlarken namaz vakitleri, dini bayramlar ve oruç dönemlerine dikkat etmek</li>
        <li><strong>Dil</strong>: faaliyetleri nasıl çerçevelediğinizde laiklik varsayımından kaçınmak</li>
        <li><strong>Kaçınmak yerine merak</strong>: din gündeme geldiğinde, herhangi bir kültürel boyuta uygulayacağınız gerçek merakla ele almak</li>
        <li><strong>Kolaylaştırıcı eğitimi</strong>: gençlik çalışanlarının yeterli arka plan bilgisine sahip olmasını sağlamak</li>
      </ul>
      <h2>Türk-Alman Boyutu</h2>
      <p>YouthTICK'in çalışmasının merkezinde yer alan Türk-Alman bağlamında din, kültürlerarası diyaloga belirli bir boyut katar. Alman-Türk gençler çoğunlukla Müslüman kimliği, laik Avrupa normları ve Türk kültürel mirasının kesişimini yüksek bireysel biçimlerde ve her iki toplumun da sıklıkla yanlış anladığı şekillerde yönetir.</p>
    """,
        'content_de': """
      <p>Religion prägt das Leben eines erheblichen Teils junger Menschen — ihre Werte, ihre Praktiken, ihr Gemeinschaftsgefühl. Dennoch behandelt die Jugendarbeit in weiten Teilen Europas Religion als Thema, das sorgfältig vermieden werden sollte: zu sensibel, zu spaltend. Diese Vermeidung ist verständlich. Sie ist auch ein Versagen des Feldes.</p>
      <h2>Warum Jugendarbeit Religion vermeidet</h2>
      <p>Die Vermeidung ist teilweise historisch. Die europäische Jugendarbeit entwickelte sich größtenteils in säkularen politischen Traditionen, die Religion als private Angelegenheit positionierten. Sie ist auch teilweise pragmatisch — Religion kann in gemischten Gruppen Konflikte erzeugen.</p>
      <blockquote>Man kann nicht behaupten, interkulturelle Dialogpraxis zu betreiben, wenn man systematisch die Erfahrungsdimension ausschließt, die für viele der jungen Menschen, mit denen man arbeitet, am zentralsten ist. Religiöse Identität ist kulturelle Identität. Die beiden sind nicht trennbar.</blockquote>
      <h2>Praktische Ansätze</h2>
      <ul>
        <li><strong>Diätetische Unterbringung</strong>: Catering mit halalen, koscheren und vegetarischen Optionen</li>
        <li><strong>Programmflexibilität</strong>: Bewusstsein für Gebetszeiten und religiöse Feste bei der Programmplanung</li>
        <li><strong>Sprache</strong>: Vermeidung von Säkularitätsannahmen in der Rahmung von Aktivitäten</li>
        <li><strong>Neugier statt Vermeidung</strong>: wenn Religion aufkommt, mit echter Neugier behandeln</li>
        <li><strong>Moderatorentraining</strong>: sicherstellen, dass Jugendarbeiter ausreichend Hintergrundwissen haben</li>
      </ul>
      <h2>Die türkisch-deutsche Dimension</h2>
      <p>Im türkisch-deutschen Kontext, der im Zentrum der Arbeit von YouthTICK steht, fügt Religion dem interkulturellen Dialog eine spezifische Dimension hinzu. Deutsch-türkische junge Menschen navigieren oft die Schnittstelle muslimischer Identität, säkularer europäischer Normen und türkischen Kulturerbes auf höchst individuelle Weise.</p>
    """
    },
    '40': {
        'title_tr': 'İkinci Nesil Gençler ve Kültürel Kimlik: İki Dünya Arasında',
        'title_de': 'Jugendliche der zweiten Generation und kulturelle Identität: Zwischen zwei Welten',
        'content_tr': """
      <p>Göçmen kökenli gençler — ebeveynlerinin doğduğu ülkede değil, başka bir ülkede büyüyenler — Avrupa toplumunda özel bir konuma sahiptir. Aynı anda birden fazla kültürel aidiyeti taşıyorlar, çoğunlukla aileleri ve geniş toplum tarafından gelen çelişkili beklentilerle başa çıkıyorlar ve sıklıkla ne "ev" kültürlerinin ne de büyüdükleri kültürün kendilerini tam anlamıyla talep etmediğini fark ediyorlar. Gençlik çalışması bu deneyimi dürüstçe ele almak için hem bir fırsata hem de bir sorumluluğa sahiptir.</p>
      <h2>"İki Dünya Arasında" Çerçevelemesi — ve Sınırları</h2>
      <p>İkinci nesil deneyimi tanımlamanın en yaygın yolu "iki dünya arasında" ifadesidir — ve bu hem kısmen doğru hem de temel biçimde yanıltıcıdır. Doğrudur çünkü diaspora gençleri çoğunlukla farklı kültürel mantıkları farklı bağlamlarda yönetir. Yanıltıcıdır çünkü iki kültürün ayrı, sınırlanmış ve uyumsuz olduğunu ima eder.</p>
      <blockquote>İkinci nesil genç yarım Türk ve yarım Alman değildir. Yeni bir şeydir — onlardan önce var olmayan ve her iki kültürün de kendi başına üretemeyeceği bir şey. Bu bir eksiklik değil, yaratıcı bir başarıdır.</blockquote>
      <h2>Gençlik Çalışmasının Yanlış Yaptıkları</h2>
      <p>İkinci nesil gençlerle gençlik çalışmasının en yaygın başarısızlığı açık çerçevelemedir: karmaşık kültürel konumlarını geliştirilen bir kaynak olarak değil, çözülmesi gereken bir sorun olarak ele almak. Entegrasyon için tasarlanan programlar çoğunlukla entegrasyonun asimilasyon anlamına geldiğini ima eder.</p>
      <h2>İyi Gençlik Çalışmasının Görünümü</h2>
      <p>İkinci nesil gençlere gerçekten hizmet eden gençlik çalışması, deneyimlerinin karmaşıklığını basitleştirmek yerine bu karmaşıklığa alan yaratır. Çoklu aidiyetleri nasıl deneyimledikleri hakkında açık sorular sorar. Melez kimliklerini bir yetkinlik olarak ele alır — gerçek ve değerli bir kültürel zeka biçimi — bir sorun olarak değil.</p>
    """,
        'content_de': """
      <p>Junge Menschen mit Migrationshintergrund — diejenigen, die in einem anderen Land aufgewachsen sind als dem Geburtsland ihrer Eltern — nehmen eine besondere Position in der europäischen Gesellschaft ein. Sie tragen mehrere kulturelle Zugehörigkeiten gleichzeitig.</p>
      <h2>Die „Zwischen zwei Welten"-Rahmung — und ihre Grenzen</h2>
      <p>Die gebräuchlichste Art, Erfahrungen der zweiten Generation zu beschreiben, ist „zwischen zwei Welten" — und das ist sowohl teilweise zutreffend als auch grundlegend irreführend. Es ist irreführend, weil es impliziert, dass die zwei Kulturen diskret, begrenzt und unvereinbar sind.</p>
      <blockquote>Der Jugendliche der zweiten Generation ist nicht halb Türke und halb Deutscher. Sie sind etwas Neues — etwas, das vor ihnen nicht existierte. Das ist eine kreative Leistung, kein Defizit.</blockquote>
      <h2>Was Jugendarbeit falsch macht</h2>
      <p>Das häufigste Versagen der Jugendarbeit mit Jugendlichen der zweiten Generation ist das Defizit-Framing: ihre komplexe kulturelle Position als zu lösendes Problem zu behandeln, anstatt als zu entwickelnde Ressource.</p>
      <h2>Wie gute Jugendarbeit aussieht</h2>
      <p>Jugendarbeit, die Jugendlichen der zweiten Generation wirklich dient, schafft Raum für die Komplexität ihrer Erfahrung, anstatt sie zu vereinfachen. Sie stellt offene Fragen darüber, wie sie ihre vielfältigen Zugehörigkeiten erleben. Sie behandelt ihre hybride Identität als Kompetenz — eine echte und wertvolle Form kultureller Intelligenz.</p>
    """
    },
    '41': {
        'title_tr': 'Yapay Zeka Çağında Dijital Vatandaşlık: Gençlik Çalışanları İçin Rehber',
        'title_de': 'Digitale Bürgerschaft im KI-Zeitalter: Ein Leitfaden für Jugendarbeiter',
        'content_tr': """
      <p>Dijital vatandaşlık eğitimi yaklaşık yirmi yıldır var. Temel müfredatı — çevrimiçi güvenlik, gizlilik ayarları, siber zorbalık farkındalığı, gerçek kontrolü — artık var olmayan bir dijital ortam için geliştirildi. Üretken YZ'nin, algoritmik öneri sistemlerinin ve YZ destekli dezenformasyonun yükselişi, eğitim çerçevelerinin uyum sağladığından daha hızlı değişti. Dijital vatandaşlık öğreten gençlik çalışanlarının bir müfredat güncellemesine ihtiyacı var.</p>
      <h2>Dijital Vatandaşlık Başlangıçta Ne Anlama Geliyordu?</h2>
      <p>2000'lerin başında geliştirilen orijinal dijital vatandaşlık çerçevesi üç alana odaklanıyordu: güvenlik, sorumluluk ve okuryazarlık. Bu çerçeve yanlış değil — sadece yetersiz. Çevrimiçi güvenlik, sorumluluk ve okuryazarlık hâlâ gereklidir. Ama artık YZ sistemleri tarafından şekillendirilen bir ortamda gezinmek için yeterli değildir.</p>
      <h2>Yeni Yetkinlikler</h2>
      <ul>
        <li><strong>Algoritmik farkındalık</strong>: çevrimiçi gördüğünüzün dünyanın tarafsız bir temsili değil, katılımınızı maksimize etmek için tasarlanmış seçilmiş bir seçki olduğunu anlamak</li>
        <li><strong>YZ okuryazarlığı</strong>: YZ sistemlerinin kavramsal düzeyde nasıl çalıştığını anlamak</li>
        <li><strong>Sentetik medya tespiti</strong>: YZ tarafından oluşturulan içeriği — görüntüler, videolar, metin — tanımlama becerisi</li>
        <li><strong>Veri sahipliği</strong>: hakkınızda hangi verilerin toplandığını, kim tarafından, hangi amaçlarla toplandığını anlamak</li>
        <li><strong>Hesaplamalı düşünme</strong>: otomatik sistemlerin nasıl karar verdiğini anlayabilme</li>
      </ul>
      <blockquote>YZ'yi ele almayan dijital vatandaşlık eğitimi, arabaları ele almayan trafik güvenliği eğitimi gibidir. Ortam değişti. Müfredat da değişmek zorunda.</blockquote>
      <h2>Gençlik Çalışanları İçin Pratik Yaklaşımlar</h2>
      <p>Gençlik çalışanlarının bu yetkinlikleri gençlerle geliştirmek için YZ uzmanı olması gerekmez. İhtiyaçları olan şey merak, belirsizlik konusunda dürüstlük ve gençleri ne sonuca varacaklarını söylemek yerine araştırmaya davet eden bir kolaylaştırma yaklaşımıdır.</p>
    """,
        'content_de': """
      <p>Digitale Bildung gibt es seit etwa zwei Jahrzehnten. Ihr Kernlehrplan — Online-Sicherheit, Datenschutzeinstellungen, Cybermobbing-Bewusstsein, Faktencheck — wurde für eine digitale Umgebung entwickelt, die nicht mehr existiert. Der Aufstieg von generativer KI hat die Landschaft schneller verändert als Bildungsrahmen sich angepasst haben. Jugendarbeiter, die Digitale Bildung unterrichten, brauchen ein Lehrplan-Update.</p>
      <h2>Was Digitale Bürgerschaft ursprünglich bedeutete</h2>
      <p>Der ursprüngliche Rahmen fokussierte auf drei Bereiche: Sicherheit, Verantwortung und Kompetenz. Dieser Rahmen ist nicht falsch — er ist einfach unzureichend.</p>
      <h2>Die neuen Kompetenzen</h2>
      <ul>
        <li><strong>Algorithmisches Bewusstsein</strong>: verstehen, dass das, was man online sieht, keine neutrale Darstellung der Welt ist</li>
        <li><strong>KI-Kompetenz</strong>: konzeptionelles Verständnis davon, wie KI-Systeme funktionieren</li>
        <li><strong>Synthethische Medienerkennung</strong>: Fähigkeiten zur Identifizierung KI-generierter Inhalte</li>
        <li><strong>Datenagentur</strong>: verstehen, welche Daten über einen gesammelt werden, von wem und für welche Zwecke</li>
        <li><strong>Rechnerisches Denken</strong>: grundlegende Fähigkeit zu verstehen, wie automatisierte Systeme Entscheidungen treffen</li>
      </ul>
      <blockquote>Digitale Bildung, die KI nicht anspricht, ist wie Straßenverkehrssicherheitsunterricht, der keine Autos anspricht. Die Umgebung hat sich verändert. Der Lehrplan muss sich mit ihr verändern.</blockquote>
      <h2>Praktische Ansätze für Jugendarbeiter</h2>
      <p>Jugendarbeiter müssen keine KI-Experten werden, um diese Kompetenzen mit jungen Menschen zu entwickeln. Was sie brauchen, ist Neugier, Ehrlichkeit über Unsicherheit und ein Moderationsansatz, der junge Menschen einlädt zu untersuchen, anstatt ihnen zu sagen, was sie schlussfolgern sollen.</p>
    """
    },
    '42': {
        'title_tr': 'Gençlik Programı Tasarımında YZ Araçlarını Kullanmak: Pratik Rehber',
        'title_de': 'KI-Tools in der Jugendprogrammgestaltung nutzen: Ein praktischer Leitfaden',
        'content_tr': """
      <p>YZ araçları, gençlik programı tasarımında gerçekten faydalı hale geldi — insan uzmanlığının ve yaratıcılığının yerine geçecek şeyler olarak değil, belirli görevlerin zaman maliyetini önemli ölçüde azaltan hızlandırıcılar olarak. Küçük, yetersiz kaynaklara sahip gençlik örgütleri için bu önemlidir. Oturum planları taslağı çizmek veya hibe başvuruları yazmak konusunda tasarruf edilen zaman, gençlerle birlikte olmak için kullanılabilir zaman demektir.</p>
      <h2>YZ Araçlarının En Çok Fayda Sağladığı Yerler</h2>
      <p>Gençlik programı tasarımındaki en zaman alan ve en formüle dayalı görevler, YZ yardımının en fazla değer kattığı görevlerdir: kısa metinden ilk oturum planları taslağı çizmek, kolaylaştırma yöntemleri için beyin fırtınası girdileri oluşturmak, hibe başvuruları için mantıksal çerçeveler yapılandırmak, materyalleri diller arasında çevirmek (insan incelemesiyle).</p>
      <h2>YZ Yazma Araçlarından En İyi Şekilde Yararlanmak</h2>
      <ul>
        <li>Bağlam sağlayın: herhangi bir istek yapmadan önce YZ'ye kim olduğunuzu, katılımcılarınızın kim olduğunu ve neyi başarmaya çalıştığınızı söyleyin</li>
        <li>Format hakkında somut olun: "dört faaliyetli 90 dakikalık atölye planı üretin" "bir atölye tasarlayın"dan çok daha iyi sonuçlar verir</li>
        <li>Yineleyin: ilk YZ çıktısını başlangıç noktası olarak değerlendirin, bitmiş ürün olarak değil</li>
        <li>Çapraz kontrol yapın: YZ araçları gerçeksel iddialar konusunda güvenle yanılabilir — istatistikler, tarihler ve politika ayrıntıları. Birincil kaynaklarla doğrulayın</li>
      </ul>
      <blockquote>En iyi YZ destekli program tasarım süreci şöyle görünür: siz vizyonu, bağlamı ve yargıyı sağlarsınız; YZ hızı, yapıyı ve ilk taslağı sağlar. İnsan her zaman editördür, YZ çıktısının pasif alıcısı değil.</blockquote>
      <h2>Etik Değerlendirmeler</h2>
      <p>Gençlik çalışmasında YZ araçlarının kullanılması, örgütlerin bireysel takdire bırakmak yerine açıkça ele alması gereken çeşitli etik soruları gündeme getirir. Veri gizliliği en acil olanıdır: uygun onay olmadan katılımcılar veya ortaklar hakkında kişisel verileri üçüncü taraf YZ sistemlerine hiçbir zaman girmeyin.</p>
    """,
        'content_de': """
      <p>KI-Tools sind für die Jugendprogrammgestaltung genutzlich geworden — nicht als Ersatz für menschliches Fachwissen und Kreativität, sondern als Beschleuniger, die den Zeitaufwand für bestimmte Aufgaben erheblich reduzieren. Für kleine, unterfinanzierte Jugendorganisationen ist das wichtig.</p>
      <h2>Wo KI-Tools am nützlichsten sind</h2>
      <p>Die zeitaufwändigsten und formulaischsten Aufgaben in der Jugendprogrammgestaltung sind auch diejenigen, bei denen KI-Unterstützung den größten Mehrwert liefert: erste Sitzungspläne entwerfen, Brainstorming-Inputs generieren, Anträge strukturieren, Materialien übersetzen.</p>
      <h2>Das Beste aus KI-Schreibwerkzeugen herausholen</h2>
      <ul>
        <li>Kontext liefern: dem KI mitteilen, wer Sie sind und was Sie zu erreichen versuchen</li>
        <li>Spezifisch bezüglich Format sein: „erstellen Sie einen 90-minütigen Workshopplan mit vier Aktivitäten" produziert weit bessere Ergebnisse</li>
        <li>Iterieren: das erste KI-Output als Ausgangspunkt behandeln, nicht als fertiges Produkt</li>
        <li>Querprüfen: KI-Tools können bei faktischen Behauptungen selbstbewusst falsch liegen</li>
      </ul>
      <blockquote>Der beste KI-gestützte Programmgestaltungsprozess sieht so aus: Sie liefern die Vision, den Kontext und das Urteil; die KI liefert Geschwindigkeit, Struktur und den ersten Entwurf. Der Mensch ist immer der Redakteur, nie der passive Empfänger von KI-Output.</blockquote>
      <h2>Ethische Überlegungen</h2>
      <p>Datenschutz ist das unmittelbarste Anliegen: Geben Sie niemals persönlich identifizierbare Informationen über Teilnehmer oder Partner in Drittanbieter-KI-Systeme ein ohne angemessene Einwilligung.</p>
    """
    },
    '43': {
        'title_tr': 'YZ Dünyasında Gençlik Çalışmasının Geleceği: Ne Değişiyor, Ne Kalıyor',
        'title_de': 'Die Zukunft der Jugendarbeit in einer KI-Welt: Was sich ändert, was bleibt',
        'content_tr': """
      <p>YZ, gençlik çalışmasını değiştirecek. Soru bunun olup olmayacağı değil, nasıl olacağı — ve gençlik çalışanlarının ve örgütlerinin değişimi iyi yönetmek için şimdi ne yapması gerektiği. Bazı şeyler otomatikleşecek. Bazı şeyler güçlendirilecek. Ve bazı şeyler, YZ'nin yapamadığı tam da bu nedenle daha önemli hale gelecek.</p>
      <h2>YZ'nin Ne Değiştireceği</h2>
      <p>Gençlik çalışmasının idari ve içerik üretimi yönleri YZ araçları tarafından zaten dönüştürülmektedir. Oturum planlaması, rapor yazma, hibe başvuruları, sosyal medya yönetimi, çeviri ve değerlendirme aracı tasarımı, YZ'nin önemli ölçüde yardımcı olabileceği görevlerdir.</p>
      <h2>YZ'nin Ne Değiştirmeyeceği</h2>
      <p>İyi gençlik çalışmasının özü — insan ilişkisi — anlamlı herhangi bir anlamda otomatikleştirilemez. Bir gencin hayatında fark yaratan şeyler — bir şeylerin yanlış olduğunu fark eden, doğru anda doğru soruyu soran, bir gencin gerçekten görüldüğünü hissettiği alan yaratan bir gençlik çalışanı — insan varlığını, empatiyi, yargıyı ve gerçek ilgiyi gerektirir.</p>
      <blockquote>Bir gençlik çalışanını etkili kılan şey oturum planları üretme veya rapor yazma yeteneği değildir. Gençlerle güven ilişkileri kurma kapasitesidir — tutarlı biçimde mevcut olmak, güvenilir biçimde dürüst olmak ve önündeki spesifik kişi hakkında gerçekten meraklı olmak. Bu derin bir insan çalışmasıdır.</blockquote>
      <h2>Daha Fazla Önem Kazanacak Beceriler</h2>
      <p>YZ daha fazla idari ve içerik görevini üstlendikçe, gençlik çalışmasının ayırt edici biçimde insani yetkinlikleri daha az değerli değil, daha değerli hale gelir: ilişkisel zeka, kolaylaştırma becerisi, etik yargı ve belirsizliği kucaklama kapasitesi.</p>
      <h2>Gençlik Örgütlerinin Şimdi Yapması Gerekenler</h2>
      <ul>
        <li>Ekipleri genelinde YZ okuryazarlığı oluşturmak</li>
        <li>YZ kullanımı konusunda açık örgütsel politikalar geliştirmek</li>
        <li>YZ tarafından arabuluculuk yapılan ortamlarda gençlerin haklarını savunmak</li>
        <li>YZ'nin kopyalayamadığı insani yetkinliklere yatırım yapmak</li>
        <li>Meraklı kalmak: YZ ortamı hızla değişiyor</li>
      </ul>
    """,
        'content_de': """
      <p>KI wird die Jugendarbeit verändern. Die Frage ist nicht ob, sondern wie — und was Jugendarbeiter und Organisationen jetzt tun müssen, um den Wandel gut zu navigieren. Einige Dinge werden automatisiert. Einige werden verstärkt. Und einige werden wichtiger, genau weil KI sie nicht kann.</p>
      <h2>Was KI verändern wird</h2>
      <p>Die administrativen und inhaltsproduzierenden Aspekte der Jugendarbeit werden bereits durch KI-Tools transformiert. Sitzungsplanung, Berichtschreiben, Förderanträge, Social-Media-Management, Übersetzung — all das sind Aufgaben, bei denen KI erheblich helfen kann.</p>
      <h2>Was KI nicht verändern wird</h2>
      <p>Der Kern guter Jugendarbeit — die menschliche Beziehung — ist in keinem bedeutsamen Sinne automatisierbar. Die Dinge, die im Leben eines jungen Menschen den Unterschied machen — ein Jugendarbeiter, der bemerkt, dass etwas nicht stimmt — erfordern menschliche Präsenz, Empathie und echte Fürsorge.</p>
      <blockquote>Was einen Jugendarbeiter effektiv macht, ist nicht ihre Fähigkeit, Sitzungspläne zu erstellen. Es ist ihre Kapazität, Vertrauensbeziehungen mit jungen Menschen aufzubauen — konsistent präsent zu sein, zuverlässig ehrlich zu sein. Das ist zutiefst menschliche Arbeit.</blockquote>
      <h2>Die Fähigkeiten, die wichtiger werden</h2>
      <p>Während KI mehr administrative und Inhaltsaufgaben übernimmt, werden die unverwechselbar menschlichen Kompetenzen der Jugendarbeit wertvoller: Beziehungsintelligenz, Moderationsfähigkeit, ethisches Urteilsvermögen.</p>
      <h2>Was Jugendorganisationen jetzt tun müssen</h2>
      <ul>
        <li>KI-Kompetenz in ihren Teams aufbauen</li>
        <li>Klare Organisationsrichtlinien zur KI-Nutzung entwickeln</li>
        <li>Für die Rechte junger Menschen in KI-vermittelten Umgebungen eintreten</li>
        <li>In die menschlichen Kompetenzen investieren, die KI nicht replizieren kann</li>
        <li>Neugierig bleiben: die KI-Landschaft verändert sich schnell</li>
      </ul>
    """
    },
    '44': {
        'title_tr': 'Avrupa Vatandaşları Girişimi: Genç Savunucular İçin Rehber',
        'title_de': 'Die Europäische Bürgerinitiative: Ein Leitfaden für junge Fürsprecher',
        'content_tr': """
      <p>Avrupa Vatandaşları Girişimi (AVG), Avrupa demokrasisinin en dikkat çekici — ve en az kullanılan — araçlarından biridir. En az yedi üye devletten bir milyon AB vatandaşının, Avrupa Komisyonu'nu AB'nin yetki alanındaki herhangi bir konuda mevzuat önermesi için davet etmesine olanak tanır.</p>
      <h2>AVG Nasıl İşler?</h2>
      <p>AVG süreci dört ana aşamadan oluşur. İlk olarak, organizatörler — en az yedi üye devletten en az yedi AB vatandaşı — girişimlerini Avrupa Komisyonu'na kaydeder. Kayıt olursa, organizatörlerin AB vatandaşlarından bir milyon imza toplamak için 12 ayları vardır; en az yedi ülkede asgari eşiklerle.</p>
      <p>Eşik karşılanırsa Komisyon girişimi incelemeli ve 6 ay içinde yanıtını — yasama önerisinde bulunup bulunmayacağını ve bulunmayacaksa neden bulunmadığını — açıklamalıdır.</p>
      <blockquote>AVG, doğrudan bir yasal mekanizma olarak değil, gündem belirleme ve siyasi baskı aracı olarak en güçlüdür. Gerçek değer kamuoyu kampanyasında yatar, resmi sonuçta değil.</blockquote>
      <h2>Başarılı AVG'ler: Deneyimden Dersler</h2>
      <p>2012'den bu yana çeşitli girişimler yeterli imzayı toplamıştır: "Right2Water" (suya erişim hakkı), "Stop Glyphosate" (herbisit), "Minority SafePack" (azınlık hakları), "End the Cage Age" (hayvan refahı).</p>
      <h2>AVG Sorununuz İçin Doğru mu?</h2>
      <p>Yatırım yapmadan önce şunu sorun: Sorununuz AB yetkisi kapsamında mı? Yedi ülkede bir milyon imza toplamak için yeterince geniş kamuoyu desteği var mı? Aynı sonuca giden daha hızlı, daha hedefli yollar var mı?</p>
    """,
        'content_de': """
      <p>Die Europäische Bürgerinitiative (EBI) ist eines der bemerkenswertesten — und am wenigsten genutzten — Instrumente der europäischen Demokratie. Sie ermöglicht es einer Million EU-Bürgern aus mindestens sieben Mitgliedstaaten, die Europäische Kommission einzuladen, Rechtsvorschriften zu einem Thema im Rahmen der EU-Zuständigkeit vorzuschlagen.</p>
      <h2>Wie die EBI funktioniert</h2>
      <p>Der EBI-Prozess hat vier Hauptphasen. Zuerst registrieren Organisatoren — mindestens sieben EU-Bürger aus mindestens sieben Mitgliedstaaten — ihre Initiative bei der Europäischen Kommission. Wenn registriert, haben Organisatoren 12 Monate, um eine Million Unterschriften zu sammeln.</p>
      <blockquote>Die EBI ist am mächtigsten als Instrument zur Agenda-Setzung und zum politischen Druck, nicht als direkter Gesetzgebungsmechanismus. Der echte Wert liegt in der öffentlichen Kampagne, nicht im formellen Ergebnis.</blockquote>
      <h2>Erfolgreiche EBIs: Lehren aus der Erfahrung</h2>
      <p>Seit Einführung der EBI 2012 haben mehrere Initiativen genügend Unterschriften gesammelt: „Right2Water", „Stop Glyphosate", „Minority SafePack", „End the Cage Age".</p>
      <h2>Ist die EBI das Richtige für Ihr Thema?</h2>
      <p>Fragen Sie sich: Fällt Ihr Thema in die EU-Zuständigkeit? Gibt es breite öffentliche Unterstützung? Haben Sie die Kapazität für eine 12-monatige EU-weite Kampagne? Gibt es schnellere, gezieltere Wege zum gleichen Ergebnis?</p>
    """
    },
    '45': {
        'title_tr': 'Avrupa Parlamentosu Üyenize Nasıl Ulaşırsınız: Genç Avrupalılar İçin Pratik Savunuculuk Rehberi',
        'title_de': 'Wie man seinen EU-Abgeordneten kontaktiert: Ein praktischer Lobbying-Leitfaden für junge Europäer',
        'content_tr': """
      <p>Avrupa Parlamentosu üyeleri, çoğu vatandaşın fark ettiğinden ortalama olarak daha erişilebilir — ve çoğu kişinin beklediğinden seçmen iletişimine daha duyarlıdır. Yaklaşık 450 milyon AB vatandaşını temsil eden 720 AP üyesiyle, bireysel AP üyesi-seçmen oranı çoğu ulusal parlamentodan daha elverişlidir. Yine de AP üyeleri gençlerden görece az doğrudan iletişim alır. Bu bir fırsattır.</p>
      <h2>AP Üyeleri Neden Meşgul Edilmeye Değer?</h2>
      <p>Avrupa Parlamentosu marjinal bir kurum değildir. Haleflik antlaşma değişiklikleri yetkilerini genişlettikten sonra Parlamento artık çoğu AB politika alanında tam bir ortak yasama organıdır — iklim, dijital düzenleme, tüketici koruma, göç, gençlik politikası. AP üyeleri bu alanları tam Parlamentoya ulaşmadan şekillendiren komitelerde oturur.</p>
      <h2>AP Üyelerinizi Bulmak</h2>
      <p>AB vatandaşları ulusal veya bölgesel seçim bölgelerinde seçilen AP üyeleri tarafından temsil edilir. AP üyelerinizi bulmak için: Avrupa Parlamentosu web sitesini (europarl.europa.eu) ziyaret edin ve "AP Üyenizi Bulun" aracını kullanın.</p>
      <h2>Etkili İletişim Nasıl Kurulur</h2>
      <ul>
        <li><strong>Önce e-posta</strong>: kendinizi tanıtan, tartışmak istediğiniz belirli konuyu adlandıran ve net bir istekte bulunan özlü bir e-posta yazın</li>
        <li><strong>Somut olun</strong>: "AB iklim politikasındaki gençlik katılımını tartışmak istiyorum" daha az etkilidir; spesifik teklifi ve komiteyi belirtin</li>
        <li><strong>Takip edin</strong>: 2 hafta sonra nezaket takip e-postası uygundur</li>
        <li><strong>Toplantı istekleri</strong>: AP üyeleri seçmen bölgesi saatleri tutar</li>
      </ul>
      <blockquote>AP üyeleri, zamanlarını mevcut çalışmalarını incelemeye ayıran seçmenlere yanıt verir. AP üyesinin son komite konuşmalarını okuyan ve konumuna atıfta bulunan savunucu, genel şablon e-posta gönderenden daha ciddiye alınır.</blockquote>
      <h2>Toplu Yaklaşımlar</h2>
      <p>Bireysel iletişim değerlidir. Aynı konu üzerinde bir gençlik örgütü, okul grubu veya gençlik konseyinden bir grup gencin koordineli iletişimi daha güçlüdür.</p>
    """,
        'content_de': """
      <p>Mitglieder des Europäischen Parlaments sind im Durchschnitt zugänglicher als die meisten Bürger erkennen — und reagieren mehr auf Wählerkontakt als die meisten Menschen erwarten. Mit 720 MdEP, die etwa 450 Millionen EU-Bürger vertreten, ist das Verhältnis MdEP-zu-Wähler günstiger als in den meisten nationalen Parlamenten.</p>
      <h2>Warum es sich lohnt, MdEPs zu engagieren</h2>
      <p>Das Europäische Parlament ist keine marginale Institution. Es ist mittlerweile vollständiger Mitgesetzgeber in den meisten EU-Politikbereichen — Klima, digitale Regulierung, Verbraucherschutz, Migration, Jugendpolitik.</p>
      <h2>Ihre MdEPs finden</h2>
      <p>Besuchen Sie die Website des Europäischen Parlaments (europarl.europa.eu) und nutzen Sie das Tool „Ihren MdEP finden".</p>
      <h2>Wie man effektiv Kontakt aufnimmt</h2>
      <ul>
        <li><strong>Zuerst E-Mail</strong>: eine prägnante, spezifische E-Mail schreiben</li>
        <li><strong>Spezifisch sein</strong>: „Ich möchte die Haltung des Parlaments zu [spezifischem Vorschlag] diskutieren"</li>
        <li><strong>Nachfassen</strong>: eine höfliche Folge-E-Mail nach 2 Wochen ist angemessen</li>
        <li><strong>Terminanfragen</strong>: MdEPs halten Wahlkreissprechstunden ab</li>
      </ul>
      <blockquote>MdEPs antworten auf Wähler, die sich die Zeit nehmen, über ihre Arbeit informiert zu sein. Der Fürsprecher, der die letzten Ausschussreden des MdEP gelesen hat, wird ernster genommen als derjenige, der eine generische Vorlagen-E-Mail sendet.</blockquote>
      <h2>Kollektive Ansätze</h2>
      <p>Individueller Kontakt ist wertvoll. Koordinierter Kontakt von einer Gruppe junger Menschen zu demselben Thema — von einer Jugendorganisation — ist mächtiger.</p>
    """
    },
    '46': {
        'title_tr': 'Katılımcı Bütçeleme: Gençler Yerel Harcamaları Kontrol Ettiğinde',
        'title_de': 'Partizipatives Budgetieren: Wenn junge Menschen lokale Ausgaben kontrollieren',
        'content_tr': """
      <p>Katılımcı bütçeleme (KB), topluluk üyelerinin bir kamu bütçesinin bir bölümünün nasıl tahsis edileceğine doğrudan karar verdiği demokratik bir süreçtir. 1989'da Brezilya'nın Porto Alegre'sinde ilk geliştirilen bu süreç, o tarihten bu yana birçok Avrupa belediyesi de dahil olmak üzere dünyadaki 3.000'den fazla şehre yayılmıştır.</p>
      <h2>Katılımcı Bütçeleme Nasıl İşler?</h2>
      <p>Tipik bir KB sürecinde bir belediye, bütçesinin tanımlı bir bölümünü — küçük bir takdir bütçesinden milyonlarca avroya kadar değişen — kamuya açık bir süreç aracılığıyla tahsis edilmek üzere ayırır. Vatandaşlar proje tekliflerini sunmaya, teklifler üzerine oy kullanmaya ve kazanan projelerin hayata geçirildiğini görmeye davet edilir. KB'yi danışmadan ayıran temel özellik, kararın bağlayıcı olmasıdır.</p>
      <h2>Gençliğe Özgü KB</h2>
      <p>Artan sayıda Avrupa şehri, genç sakinlerin (çoğunlukla 14-26) ayrılmış bir gençlik bütçesinin tahsisi konusunda karar verdiği gençlere özgü KB süreçleri yürütmektedir. Bu süreçler Paris, Lizbon, Gdańsk ve Reykjavik gibi şehirlerde yürütülmüştür.</p>
      <blockquote>Gençlik KB "sahte demokrasi" değildir — yetişkinlerin görmezden gelebileceği bir istişare. Gerçek demokrasidir: gençlerin seçtiği projeler inşa edilir. Bu onun hakkındaki en güçlü şeydir. Gençler istişare edilmek ile gerçekten karar vermek arasındaki farkı bilir.</blockquote>
      <h2>Etki Kanıtı</h2>
      <p>Katılımcı bütçeleme araştırmaları tutarlı biçimde olumlu sonuçlar göstermektedir. Katılımcılar daha yüksek sivil bilgi, kamu kurumlarıyla etkileşimde daha fazla özgüven ve yerel yönetime artan güven bildiriyor — ancak yalnızca süreç gerçek olduğunda ve sonuçlar hayata geçirildiğinde.</p>
      <h2>Bağlamınızda Gençlik KB Başlatmak</h2>
      <p>Belediyelerinde gençlik KB'sini savunan gençlik örgütleri için en etkili yaklaşım, tam tasarlanmış bir programdan ziyade küçük, başarılı bir pilot başlatmaktır. Küçük ama mütevazı bir bütçe (5.000-10.000 € bile anlamlı bir ilk süreç yürütebilir), basit ve erişilebilir bir süreç tasarlayın ve kazanan projelerin gerçekten hayata geçirildiğinden emin olun.</p>
    """,
        'content_de': """
      <p>Partizipatives Budgetieren (PB) ist ein demokratischer Prozess, bei dem Gemeindemitglieder direkt entscheiden, wie ein Teil eines öffentlichen Budgets zugewiesen wird. Erstmals 1989 in Porto Alegre, Brasilien, entwickelt, hat es sich seitdem auf mehr als 3.000 Städte weltweit ausgebreitet — darunter viele europäische Kommunen.</p>
      <h2>Wie partizipatives Budgetieren funktioniert</h2>
      <p>In einem typischen PB-Prozess weist eine Kommune einen definierten Teil ihres Budgets zu, der durch einen öffentlichen Prozess zugeteilt werden soll. Bürger werden eingeladen, Projektvorschläge einzureichen, über eingereichte Vorschläge abzustimmen und zu sehen, wie Gewinnerprojekte umgesetzt werden. Das entscheidende Merkmal, das PB von Konsultation unterscheidet, ist, dass die Entscheidung bindend ist.</p>
      <h2>Jugendspezifisches PB</h2>
      <p>Eine zunehmende Anzahl europäischer Städte führt PB-Prozesse speziell für junge Menschen durch. Diese Prozesse wurden in Städten wie Paris, Lissabon, Gdańsk und Reykjavik durchgeführt.</p>
      <blockquote>Jugend-PB ist keine „Pseudo-Demokratie" — eine Konsultation, die Erwachsene ignorieren können. Es ist echte Demokratie: Die Projekte, die junge Menschen wählen, werden gebaut. Das ist das Mächtigste daran. Junge Menschen kennen den Unterschied zwischen konsultiert werden und wirklich entscheiden.</blockquote>
      <h2>Belege der Wirkung</h2>
      <p>Forschungen zu partizipativem Budgetieren zeigen konsistent positive Ergebnisse: Teilnehmer berichten über höhere Niveaus staatsbürgerlichen Wissens, größeres Vertrauen in lokale Regierung — aber nur wenn der Prozess echt ist und die Ergebnisse umgesetzt werden.</p>
      <h2>Ein Jugend-PB in Ihrem Kontext starten</h2>
      <p>Für Jugendorganisationen, die für Jugend-PB in ihrer Kommune eintreten, ist der effektivste Ansatz, mit einem kleinen, erfolgreichen Pilotprojekt zu beginnen. Finden Sie einen sympathischen lokalen Stadtrat, identifizieren Sie ein bescheidenes Budget (sogar 5.000–10.000 € kann einen bedeutungsvollen ersten Prozess ermöglichen), gestalten Sie einen einfachen, zugänglichen Prozess und setzen Sie ihn rigoros um.</p>
    """
    },
}

for art_id, trans in translations.items():
    pattern = rf"(  '{art_id}': {{.*?content: `.*?`)"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  ✗ Article {art_id} — not found")
        continue
    insert_pos = match.end()
    insert_str = (
        f",\n    title_tr: `{trans['title_tr']}`"
        f",\n    title_de: `{trans['title_de']}`"
        f",\n    content_tr: `{trans['content_tr']}`"
        f",\n    content_de: `{trans['content_de']}`"
    )
    content = content[:insert_pos] + insert_str + content[insert_pos:]
    print(f"  ✓ Article {art_id}")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
