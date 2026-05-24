#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adds TR/DE translations to articles 1-15 in articles.js"""

import re

TRANS = {
'1': {
'title_tr': "Gençlik Öncülüğündeki Girişimler Avrupa'da Sosyal Etkiyi Yeniden Tanımlıyor",
'title_de': "Jugendgeführte Startups definieren sozialen Impact in Europa neu",
'content_tr': """
      <p>Avrupa'daki gençlik girişimciliğinde bir şeyler değişiyor. Birçoğu 25 yaşın altında olan yeni bir kurucu dalgası, kâr ile amacı zıtlar olarak değil, ortaklar olarak gören şirketler kuruyor. Bu idealizm değil, strateji.</p>
      <h2>Değişimin Arkasındaki Veriler</h2>
      <p>Avrupa Gençlik Forumu'nun son araştırmasına göre, kendini girişimci olarak tanımlayan genç Avrupalıların neredeyse %40'ı sosyal veya çevresel etkiyi temel motivasyonları olarak görüyor — finansal kazancın önünde. Bu oran on yıl önce %20'nin altındaydı.</p>
      <p>İnşa ettikleri kuruluşlar bunu yansıtıyor. B Corp sertifikası, toplum yararı maddeleri, şeffaf ücret oranları, açık kaynak modeller — bunlar artık istisna değil. Birçok genç kurucu için bunlar başlangıç çıtasıdır.</p>
      <h2>Bu Neden Şimdi Oluyor?</h2>
      <p>Birkaç güç bir araya geliyor. İklim krizi çevresel maliyetleri somut ve kişisel hale getirdi. Pandemi, soyut kavramları gerçek kılan biçimlerde sistemsel kırılganlıkları gözler önüne serdi. Dijital araçların yaygınlaşması ise bir şeyler başlatmanın önündeki engelleri dramatik biçimde düşürdü.</p>
      <blockquote>2026'da sosyal bir girişim kurmak için işletme okulu diplomasına ihtiyacınız yok. Çözülmeye değer bir soruna, yardım etmeye istekli bir ağa ve kimse bakmazken devam edecek azme ihtiyacınız var.</blockquote>
      <h2>Bu Gençlik Kuruluşları İçin Ne Anlama Geliyor</h2>
      <p>Genç insanlarla çalışan kuruluşlar için bu değişim hem bir fırsat hem de bir sorumluluk doğuruyor. Gençler, kurumların onlar için yol açmasını beklemiyor; kendi yollarını inşa ediyorlar. Soru şu: Köklü kurumlar bu enerjiye alan açacak mı, yoksa gençleri geleneksel kariyer yollarına yönlendirmeye devam mı edecek?</p>
      <p>YouthTICK olarak, programlarımız çerçevesinde gençlik öncülüğündeki inovasyonu nasıl destekleyebileceğimizi araştırıyoruz — belirlenmiş çıktıları olan bir proje olarak değil, mevcut duruma meydan okuyan fikirlere gerçek anlamda alan açma taahhüdü olarak.</p>
""",
'content_de': """
      <p>Im europäischen Jugendunternehmertum verändert sich etwas. Eine neue Welle von Gründerinnen und Gründern — viele davon unter 25 — baut Unternehmen auf, die Profit und Zweck nicht als Gegensätze, sondern als Partner betrachten. Das ist kein Idealismus. Es ist Strategie.</p>
      <h2>Die Daten hinter dem Wandel</h2>
      <p>Laut aktueller Forschung des Europäischen Jugendforums geben fast 40% der jungen Europäerinnen und Europäer, die sich als Unternehmer identifizieren, an, dass sozialer oder ökologischer Impact ihr primäres Motiv ist — noch vor dem finanziellen Gewinn. Vor einem Jahrzehnt lag diese Zahl unter 20%.</p>
      <p>Die Organisationen, die sie aufbauen, spiegeln dies wider. B Corp-Zertifizierung, Gemeinwohlklauseln, transparente Lohnquoten, Open-Source-Modelle — das sind nicht mehr die Ausnahme. Für viele junge Gründer ist das die Grundlage.</p>
      <h2>Warum passiert das jetzt?</h2>
      <p>Mehrere Kräfte konvergieren. Die Klimakrise hat Umweltkosten konkret und persönlich gemacht. Die Pandemie hat systemische Fragilität auf eine Weise offenbart, die abstrakte Konzepte real werden ließ. Und die Verfügbarkeit digitaler Werkzeuge hat die Hürden für einen Unternehmensstart erheblich gesenkt.</p>
      <blockquote>Sie brauchen 2026 keinen Business-School-Abschluss, um ein Sozialunternehmen zu gründen. Sie brauchen ein Problem, das es wert ist, gelöst zu werden, ein Netzwerk, das bereit ist zu helfen, und die Beharrlichkeit, weiterzumachen, wenn niemand zuschaut.</blockquote>
      <h2>Was das für Jugendorganisationen bedeutet</h2>
      <p>Für Organisationen, die mit jungen Menschen arbeiten, schafft dieser Wandel sowohl eine Chance als auch eine Verantwortung. Junge Menschen warten nicht darauf, dass Institutionen Wege für sie schaffen — sie bauen ihre eigenen. Die Frage ist, ob etablierte Institutionen Raum für diese Energie schaffen oder junge Menschen weiterhin in konventionelle Karrierewege lenken.</p>
      <p>Bei YouthTICK erkunden wir, wie wir jugendgeführte Innovation im Rahmen unserer Programme unterstützen können — nicht als Projekt mit definierten Ergebnissen, sondern als echtes Engagement dafür, Ideen Raum zu geben, die den Status quo herausfordern.</p>
"""
},
'2': {
'title_tr': "Yeşil Nesil: Gençler İklim Politikasını Nasıl Yönlendiriyor",
'title_de': "Die grüne Generation: Wie junge Menschen die Klimapolitik vorantreiben",
'content_tr': """
      <p>Gençlik iklim savunuculuğu yıllarca sembolik olarak nitelendirildi — duygusal açıdan güçlü, siyasi açıdan marjinal. Bu değişiyor. Genç iklim savunucuları artık resmi müzakerelerde oturuyor, hükümet bakanlıklarına danışmanlık yapıyor ve AB düzeyinde fon alan kuruluşlara önderlik ediyor.</p>
      <h2>Sokaktan Kurumlara</h2>
      <p>Protestodan politikaya geçiş bir gecede olmadı. Sürdürülen kamuoyu baskısı, kurumlarda gençlik katılımına yönelik artan açıklık ve iklim politikasının gençlik sesleri olmadan ne siyasi ne de pratik açıdan sağlam olmadığının giderek kabul edilmesinin ardından geldi.</p>
      <p>Önemli dönüm noktaları: Avrupa Gençlik İklim Koalisyonu'nun COP süreçlerine katılımı; gençlik delegelerinin ulusal heyetlere dahil edilmesi; Avrupa Komisyonu'nun Yeşil Mutabakat uygulamasında gençlik katılımına dair resmi taahhüdü.</p>
      <h2>Genç Savunucuların Talepleri</h2>
      <p>Talepler olgunlaştı. Erken dönem gençlik iklim savunuculuğu farkındalık yaratmaya ve harekete geçme çağrısına odaklanıyordu. Bugünün genç iklim liderleri somut politika araçları üzerinde çalışıyor: emisyon fiyatlandırması, tarımsal geçiş desteği, döngüsel ekonomi standartları ve fosil yakıt topluluklarına yönelik adil geçiş mekanizmaları.</p>
      <blockquote>İlham kaynağı olmak için burada değiliz. Çalışmak için buradayız. Bu, politika sürecini anlamamız, koalisyonlar kurmamız ve durum rahatsız edici hale geldiğinde odada kalmamız gerektiği anlamına geliyor.</blockquote>
      <h2>Türkiye Bağlamı</h2>
      <p>Türkiye'de gençlik iklim katılımı büyüyor — ancak kendine özgü zorluklarla karşılaşıyor. Resmi savunuculuk kanallarına sınırlı erişim, gelişmekte olan sivil toplum sektörü ve çevre politikasının karmaşıklığı engeller oluşturuyor. Ancak gençler yaratıcı katılım yolları buluyor: yerel yönetim, sosyal medya kampanyaları ve Avrupa gençlik ağlarıyla bağlantılar aracılığıyla.</p>
      <p>YouthTICK'in sürdürülebilirlik programı, Yalova'daki gençlerin bu konularla yerel, ulusal ve nihayetinde Avrupa düzeyinde ilgilenmeleri için hem bilgi hem de güven geliştirmelerini desteklemeyi amaçlıyor.</p>
""",
'content_de': """
      <p>Jugendklimaaktivismus wurde jahrelang als symbolisch abgetan — emotional stark, politisch marginal. Das ändert sich. Junge Klimaaktivisten sitzen jetzt in formellen Verhandlungen, beraten Regierungsministerien und leiten Organisationen, die EU-Förderung erhalten.</p>
      <h2>Von der Straße in die Institutionen</h2>
      <p>Der Wandel vom Protest zur Politik geschah nicht über Nacht. Er folgte einer Phase anhaltenden öffentlichen Drucks, wachsender institutioneller Offenheit für Jugendbeteiligung und der schrittweisen Anerkennung, dass Klimapolitik ohne Jugendstimmen weder politisch noch praktisch solide ist.</p>
      <p>Wichtige Wendepunkte: die Beteiligung der European Youth Climate Coalition an COP-Prozessen; die Einbeziehung von Jugenddelegierten in nationale Delegationen; und das formelle Engagement der Europäischen Kommission für die Jugendbeteiligung bei der Umsetzung des Green Deal.</p>
      <h2>Was junge Aktivisten fordern</h2>
      <p>Die Forderungen haben sich entwickelt. Früher Jugendklimaaktivismus konzentrierte sich auf Bewusstseinsbildung und Forderungen nach Maßnahmen. Die heutigen jungen Klimaführer arbeiten an spezifischen Politikinstrumenten: Emissionsbepreisung, Unterstützung für den Agrarübergang, Kreislaufwirtschaftsstandards und Mechanismen für einen gerechten Übergang für Gemeinschaften, die von fossilen Brennstoffen abhängig sind.</p>
      <blockquote>Wir sind nicht hier, um Inspiration zu sein. Wir sind hier, um zu arbeiten. Das bedeutet, wir müssen den Politikprozess verstehen, Koalitionen aufbauen und im Raum bleiben, wenn es unangenehm wird.</blockquote>
      <h2>Der türkische Kontext</h2>
      <p>In der Türkei wächst das Engagement junger Menschen für das Klima — steht aber vor spezifischen Herausforderungen. Eingeschränkter Zugang zu formellen Advocacy-Kanälen, ein junger Zivilgesellschaftssektor und die Komplexität der Umweltpolitik schaffen Barrieren. Aber junge Menschen finden kreative Wege zur Beteiligung: durch lokale Verwaltung, Social-Media-Kampagnen und Verbindungen zu europäischen Jugendbewegungen.</p>
      <p>YouthTICKs Nachhaltigkeitsprogramm zielt darauf ab, junge Menschen in Yalova dabei zu unterstützen, sowohl das Wissen als auch das Vertrauen zu entwickeln, um sich mit diesen Themen zu beschäftigen — lokal, national und schließlich auf europäischer Ebene.</p>
"""
},
'3': {
'title_tr': "Kültürlerarası Diyalog Gerçekte Nasıl Görünür (İpucu: Dağınık)",
'title_de': "Wie interkultureller Dialog wirklich aussieht (Hinweis: Es ist unordentlich)",
'content_tr': """
      <p>Sekiz yıldır gençlik eğitmeni olarak çalışıyorum. On iki ülkede, kırkı aşkın ülkeden katılımcıyla değişimler kolaylaştırdım. Her gruba başlamadan önce şunu söylerim: kültürlerarası diyalog kendini iyi hissettiren bir egzersiz değildir. Bir pratiktir. Pratikler ise rahatsız edicidir.</p>
      <h2>Pürüzsüz Değişim Efsanesi</h2>
      <p>Gençlik değişimlerinden fotoğraflar güzeldir. Gülen gençler, paylaşılan yemekler, bayraklar ve dostluk bilezikleri. Bu anlar gerçektir. Ancak bunlar çok daha karmaşık — ve çok daha değerli — bir şeyin yüzeyidir.</p>
      <p>Gerçek çalışma, üçüncü gündeki atölyede biri kültürler arasında farklı yankılanan bir şey söylediğinde gerçekleşir. Cinsiyet rolleri, aile yapıları ya da siyasi tarih hakkındaki varsayımlar grup tartışmasının ortasında çarpıştığında gerçekleşir. Bir şaka çevrilmediğinde — ya da çok iyi çevrildiğinde — gerçekleşir.</p>
      <h2>İyi Kolaylaştırma Nasıl Görünür</h2>
      <p>İyi kolaylaştırma bu anları düzeltmez. Onlar için alan yaratır. Deneyimli bir gençlik eğitmeni bir oturumu nasıl durduracağını, yaşananı nasıl adlandıracağını, farklı bakış açılarını nasıl davet edeceğini ve grubu yapay bir çözüme zorlamadan yansımaya nasıl yönlendireceğini bilir.</p>
      <blockquote>Amaç herkesin hemfikir olması değildir. Amaç herkesin anlamasıdır — neden ayrı düştüklerini ve bu ayrılığın neden önemli olduğunu anlamak da dahil.</blockquote>
      <h2>Türk-Alman Boyutu</h2>
      <p>Türk ve Alman katılımcıları içeren birkaç değişim kolaylaştırdım. Bu topluluklar arasındaki tarih — göç, emek, siyaset ve kültür tarafından şekillendirilen — diyalog için zengin bir zemin oluşturur. Aynı zamanda mayın tarlaları da yaratır.</p>
      <p>Bu bağlamda verimli diyalog hazırlık gerektirir: katılımcıların kilit konularda ortak bir sözcük dağarcığına sahip olmasını sağlamak, farklılıklar üzerinden nasıl iletişim kurulacağına dair uzlaşılar oluşturmak ve insanların söylemeleri gerektiğini düşündüklerini değil, gerçekten düşündüklerini söyleyebilmeleri için yeterli psikolojik güvenlik yaratmak.</p>
      <p>YouthTICK'te bu hedef doğrultusunda çalışıyoruz: performatif biçimde uyumlu değil, gerçek anlamda diyalogsal bir değişim. Daha fazla hazırlık gerektirir ve daha fazla risk taşır. Ama kalıcı değişim yaratır.</p>
""",
'content_de': """
      <p>Ich bin seit acht Jahren Jugendtrainer. Ich habe Austausche in zwölf Ländern facilitiert, mit Teilnehmenden aus über vierzig. Und was ich jeder Gruppe vor Beginn sage, ist Folgendes: Interkultureller Dialog ist keine Wohlfühlübung. Es ist eine Praxis. Und Praktiken sind unbequem.</p>
      <h2>Der Mythos des reibungslosen Austauschs</h2>
      <p>Die Fotos von Jugendbegegnungen sind schön. Lachende junge Menschen, gemeinsame Mahlzeiten, Flaggen und Freundschaftsarmbänder. Diese Momente sind real. Aber sie sind die Oberfläche von etwas viel Komplexerem — und viel Wertvolleren.</p>
      <p>Die eigentliche Arbeit geschieht im Workshop am dritten Tag, wenn jemand etwas sagt, das in verschiedenen Kulturen unterschiedlich ankommt. Sie geschieht, wenn Annahmen über Geschlechterrollen, Familienstrukturen oder politische Geschichte mitten in einer Gruppendiskussion aufeinanderprallen. Sie geschieht, wenn ein Witz nicht übersetzt — oder zu gut übersetzt wird.</p>
      <h2>Wie gute Facilitation aussieht</h2>
      <p>Gute Facilitation glättet diese Momente nicht. Sie schafft Raum für sie. Ein erfahrener Jugendtrainer weiß, wie man eine Sitzung unterbricht, benennt, was passiert ist, verschiedene Perspektiven einlädt und die Gruppe zu Reflexion führt, ohne eine falsche Lösung zu erzwingen.</p>
      <blockquote>Das Ziel ist nicht, dass alle zustimmen. Das Ziel ist, dass alle verstehen — einschließlich des Verständnisses, warum sie nicht einer Meinung sind, und warum diese Meinungsverschiedenheit wichtig ist.</blockquote>
      <h2>Die deutsch-türkische Dimension</h2>
      <p>Ich habe mehrere Austausche mit türkischen und deutschen Teilnehmenden facilitiert. Die Geschichte zwischen diesen Gemeinschaften — geprägt durch Migration, Arbeit, Politik und Kultur — schafft reichhaltiges Terrain für Dialog. Sie schafft auch Minenfelder.</p>
      <p>Produktiver Dialog in diesem Kontext erfordert Vorbereitung: sicherstellen, dass die Teilnehmenden ein gemeinsames Vokabular zu Schlüsselthemen haben, Vereinbarungen darüber treffen, wie man mit Unterschieden umgeht, und genug psychologische Sicherheit schaffen, damit Menschen sagen können, was sie wirklich denken.</p>
      <p>Bei YouthTICK ist das unser Ziel: ein Austausch, der wirklich dialogisch ist, nicht performativ harmonisch. Es erfordert mehr Vorbereitung und birgt mehr Risiken. Aber es schafft dauerhaften Wandel.</p>
"""
},
'4': {
'title_tr': "Bir Gençlik Hakkı Olarak Yapay Zeka Okuryazarlığı: Dijital Eşitliğe Neden Şimdi İhtiyacımız Var",
'title_de': "KI-Kompetenz als Jugendrecht: Warum wir jetzt digitale Gerechtigkeit brauchen",
'content_tr': """
      <p>Yapay zeka artık bir gelecek teknolojisi değil. İşe alım, eğitim, sağlık, kredi erişimi ve sivil katılımı halihazırda yeniden şekillendiriyor. Yapay zeka okuryazarlığına erişim — yapay zeka sistemlerini anlama, kullanma ve eleştirel biçimde değerlendirme yeteneği — neslimizin belirleyici eşitsizliği haline geliyor.</p>
      <h2>Yapay Zeka Okuryazarlığı Nedir?</h2>
      <p>Yapay zeka okuryazarlığı kod yazmayı öğrenmekle aynı şey değildir. Şunları kapsar: yapay zeka sistemlerinin nasıl karar verdiğini (ve bu kararları kimin tasarladığını) anlama, modellere gömülü sınırlamaları ve önyargıları tanıma, yapay zeka araçlarını etkili ve eleştirel biçimde kullanma, yapay zeka yönetişimi hakkındaki kamusal tartışmaya katılma.</p>
      <p>İyi donanımlı eğitim ortamlarındaki gençler bunun bir kısmını almaya başlıyor. Az kaynaklı ortamlardaki gençler — özellikle daha az gelişmiş dijital altyapıya sahip ülkelerde — almıyor.</p>
      <h2>Eşitlik Uçurumu</h2>
      <p>Dijital uçurum yeni değil. Ama yapay zeka onu özgün biçimlerde büyütüyor. Yapay zeka destekli işe alım araçları, bir insan görmeden önce özgeçmişleri tarar. Kredi algoritmaları kimin kredi alacağını belirler. İçerik öneri sistemleri insanların hangi bilgileri alacağını şekillendirir. Bu sistemleri anlayamazsanız, onlar içinde kendiniz için etkili biçimde savunuculuk yapamazsınız.</p>
      <blockquote>İki kademeli bir dünya yaratıyoruz: yapay zeka sistemlerini anlayan ve stratejik biçimde yönlendirebilenlere karşı, bu sistemlere geri itme araçları olmadan tabi olanlar.</blockquote>
      <h2>Gençlik Kuruluşları Ne Yapabilir</h2>
      <p>Gençlik kuruluşları önemli bir kavşakta yer alıyor. Resmi eğitim veya istihdamda olmayan gençlere erişimleri var. Karmaşık konuları erişilebilir kılacak yaygın eğitim uzmanlıkları var. Ve zor sorularda gerçek katılım için gerekli güven ilişkileri var.</p>
      <p>YouthTICK olarak yapay zeka okuryazarlığını programlarımıza nasıl entegre edeceğimizi araştırıyoruz — teknik bir modül olarak değil, sivil bir yetkinlik olarak. Yapay zekayı anlamak mesleki bir beceri değil. Vatandaşlık becerisidir. Ve her genç bunu hak ediyor.</p>
""",
'content_de': """
      <p>Künstliche Intelligenz ist keine Zukunftstechnologie mehr. Sie verändert bereits Einstellung, Bildung, Gesundheitsversorgung, Kreditvergabe und Bürgerbeteiligung. Der Zugang zu KI-Kompetenz — die Fähigkeit, KI-Systeme zu verstehen, zu nutzen und kritisch zu bewerten — wird zur bestimmenden Ungleichheit unserer Generation.</p>
      <h2>Was KI-Kompetenz ist</h2>
      <p>KI-Kompetenz ist nicht dasselbe wie das Erlernen des Programmierens. Sie umfasst: zu verstehen, wie KI-Systeme Entscheidungen treffen (und wer diese Entscheidungen gestaltet hat), die in Modellen eingebetteten Einschränkungen und Vorurteile zu erkennen, KI-Tools effektiv und kritisch zu nutzen und an öffentlichen Debatten über KI-Governance teilzunehmen.</p>
      <p>Junge Menschen in gut ausgestatteten Bildungsumgebungen beginnen, einen Teil davon zu erhalten. Junge Menschen in unterversorgten Umgebungen — insbesondere in Ländern mit weniger entwickelter digitaler Infrastruktur — nicht.</p>
      <h2>Die Gerechtigkeitslücke</h2>
      <p>Die digitale Kluft ist nicht neu. Aber KI verstärkt sie auf spezifische Weisen. KI-gestützte Einstellungstools durchsuchen Lebensläufe, bevor ein Mensch sie jemals sieht. Kreditalgorithmen bestimmen, wer Darlehen erhält. Content-Empfehlungssysteme prägen, welche Informationen Menschen erhalten. Wenn man diese Systeme nicht versteht, kann man innerhalb von ihnen nicht effektiv für sich selbst eintreten.</p>
      <blockquote>Wir schaffen eine zweistufige Welt: diejenigen, die KI-Systeme verstehen und strategisch navigieren können, und diejenigen, die diesen Systemen unterworfen sind, ohne die Werkzeuge, um zurückzudrücken.</blockquote>
      <h2>Was Jugendorganisationen tun können</h2>
      <p>Jugendorganisationen befinden sich an einem wichtigen Schnittpunkt. Sie haben Zugang zu jungen Menschen, die sich nicht in formeller Bildung oder Beschäftigung befinden. Sie verfügen über das non-formale Bildungsexpertise, um komplexe Themen zugänglich zu machen. Und sie haben die Vertrauensbeziehungen, die für echtes Engagement bei schwierigen Fragen nötig sind.</p>
      <p>Bei YouthTICK erkunden wir, wie KI-Kompetenz in unsere Programme integriert werden kann — nicht als technisches Modul, sondern als bürgerliche Kompetenz. KI zu verstehen ist keine berufliche Fähigkeit. Es ist eine Bürgerkompetenz. Und jeder junge Mensch verdient sie.</p>
"""
},
'5': {
'title_tr': "Z Kuşağı Neden 1960'lardan Bu Yana Her Nesilden Daha Siyasi Olarak Aktif",
'title_de': "Warum die Gen Z politisch aktiver ist als jede Generation seit den 1960ern",
'content_tr': """
      <p>Gençler ve siyaset hakkındaki anlatı inatla süregeldi: Z Kuşağı ilgisiz, sosyal medyayla dikkatini dağıtmış, sivil yaşama ilgisiz. Yeni araştırmalar bu anlatının yalnızca yanlış olmadığını — tam tersinin doğru olduğunu — ortaya koyuyor.</p>
      <h2>Veriler</h2>
      <p>Avrupa Konseyi'nin gençlik sektörü tarafından 40 ülkeden veri alınarak yapılan 2025 tarihli bir çalışma, 18-25 yaş arasındakilerin son altmış yılda ölçülen herhangi bir yaş kohortundan daha yüksek siyasi ilgi, sivil katılım ve kolektif eylem katılımı düzeyleri bildirdiğini buldu. Bu katılımın biçimi farklı. Ama yoğunluğu değil.</p>
      <p>Değişen şey alandır. Gençler siyasi partilere katılmadıkları için daha az siyasi olarak aktif değiller. Çevrimiçi hareketler, tüketici boykotları, toplum örgütlenmesi ve doğrudan sivil eylem yoluyla daha aktifler.</p>
      <h2>Mit Neden Süregeliyor</h2>
      <p>İlgisizlik miti, yanlış araçlarla ölçüldüğü için süregeliyor. Seçim katılımı — geleneksel ölçüt — gerçek bir olguyu yansıtıyor: gençler yaşlı kohortlara kıyasla daha düşük oranlarda oy kullanıyor. Ama bu kısmen yapısal bir sorun (kayıt engelleri, çalışma saatleri, sandık yerleri) ve kısmen de değişimin birincil modu olarak seçim siyasetine azalan güvenin yansımasıdır.</p>
      <blockquote>Gençler siyasetten uzak değil. Sadece geleneksel siyaset biliminin bakmadığı yerlere taşındılar.</blockquote>
      <h2>Bu Gençlik Katılım Programları İçin Ne Anlama Geliyor</h2>
      <p>Gençler zaten siyasi olarak meşgulse — sadece geleneksel olmayan biçimlerde — gençlik katılım programları açık uçlu bir modelden başlamamalıdır. Gençlerin bulunduğu yerden başlamalıdır. Zaten var olan sivil kimliğin üzerine inşa etmeli. Resmi yapılarla bağlantı kurmalı. Köprüler oluşturmalı — aşağıdan yukarıya değil, yatay olarak.</p>
      <p>YouthTICK'te sivil katılım programımız bu öncülden başlıyor. Yalova'daki gençler harekete geçirilmeyi beklemiyor. Yaşamlarını etkileyen konularla zaten ilgileniyorlar. Bizim işimiz bu katılımın daha görünür, daha bağlantılı ve daha güçlü hale gelmesi için koşullar yaratmak.</p>
""",
'content_de': """
      <p>Die Erzählung über junge Menschen und Politik war hartnäckig: Die Generation Z ist apathisch, durch soziale Medien abgelenkt, am bürgerlichen Leben uninteressiert. Neue Forschungsergebnisse legen nahe, dass diese Erzählung nicht nur falsch ist — sie ist genau umgekehrt.</p>
      <h2>Die Daten</h2>
      <p>Eine Studie aus dem Jahr 2025 vom Jugendsektor des Europarats, die Daten aus 40 Ländern auswertete, stellte fest, dass 18- bis 25-Jährige höhere Werte bei politischem Interesse, bürgerlichem Engagement und Teilnahme an kollektiver Aktion angeben als jede in den letzten sechzig Jahren gemessene Altersgruppe. Die Form dieses Engagements ist anders. Aber die Intensität ist es nicht.</p>
      <p>Was sich verändert hat, ist der Schauplatz. Junge Menschen sind nicht weniger politisch aktiv, weil sie politischen Parteien nicht beitreten. Sie sind aktiver durch Online-Bewegungen, Verbraucherboykotts, Community-Organisierung und direkte bürgerliche Aktion.</p>
      <h2>Warum der Mythos fortbesteht</h2>
      <p>Der Apathie-Mythos hält sich, weil er mit den falschen Werkzeugen gemessen wird. Die Wahlbeteiligung — das traditionelle Maß — erfasst zwar ein reales Phänomen: Junge Menschen wählen seltener als ältere Kohorten. Aber das ist teils ein strukturelles Problem und teils eine Reflexion des sinkenden Vertrauens in die Wahlpolitik als primärer Änderungsmodus.</p>
      <blockquote>Junge Menschen sind nicht abwesend von der Politik. Sie sind einfach an Orte gezogen, wo die traditionelle Politikwissenschaft nicht hingeschaut hat.</blockquote>
      <h2>Was das für Jugendbeteiligungsprogramme bedeutet</h2>
      <p>Wenn junge Menschen bereits politisch engagiert sind — nur auf nicht-traditionelle Weisen — sollten Jugendbeteiligungsprogramme nicht von einem Defizitmodell ausgehen. Sie sollten dort anfangen, wo junge Menschen sind. Auf der bereits vorhandenen bürgerlichen Identität aufbauen. Sie mit formellen Strukturen verbinden. Brücken bauen — nicht von unten nach oben, sondern seitwärts.</p>
      <p>Bei YouthTICK beginnt unser Bürgerbeteiligungsprogramm mit dieser Prämisse. Junge Menschen in Yalova warten nicht darauf, aktiviert zu werden. Sie sind bereits mit den Themen beschäftigt, die ihr Leben betreffen. Unsere Aufgabe ist es, die Bedingungen zu schaffen, damit dieses Engagement sichtbarer, vernetzter und wirkungsvoller wird.</p>
"""
},
'6': {
'title_tr': "Doğru Erasmus+ Ortakları Nasıl Bulunur (6 Ay Harcamadan)",
'title_de': "Wie man die richtigen Erasmus+-Partner findet (ohne 6 Monate zu verschwenden)",
'content_tr': """
      <p>Erasmus+ projeleri için uluslararası ortaklıklar kurmak, gençlik çalışmasının en ödüllendirici — ve en sinir bozucu — parçalarından biridir. İyi yapıldığında yıllarca süren ilişkiler ve katılımcıların hayatını gerçek anlamda değiştiren projeler ortaya çıkar. Kötü yapıldığında aylarca e-posta alışverişi boşa gider ve proje başvuru aşamasında çöker.</p>
      <h2>Coğrafyadan Değil Değerlerden Başlayın</h2>
      <p>En yaygın hata, ortaklık kurmayı lojistik bir egzersiz olarak ele almaktır. Almanya'dan bir ortağa ihtiyacınız var (fon kuralları için). Ev sahibi olabilecek bir ortağa ihtiyacınız var. Finansal raporlamayı yönetebilecek bir ortağa ihtiyacınız var. Bunların hepsi doğru — ama buradan başlarsanız, teknik olarak uyumlu ama tematik olarak uyumsuz kuruluşlarla sonuçlanırsınız.</p>
      <p>Şundan başlayın: bu proje gerçekte neyle ilgili? Hangi değerleri ve yaklaşımları gerektiriyor? Başka ülkelerde benzer enerji ve bütünlükle bu sorular üzerinde kim çalışıyor? Sonra coğrafyayla ilgilenin.</p>
      <h2>Ortakları Gerçekten Nerede Bulabilirsiniz</h2>
      <p>SALTO Ortaklık Aracı (TCA) en kapsamlı veri tabanıdır, ancak en iyi ortaklıkların geldiği yer burası değildir. En iyi ortaklıklar eğitim kurslarında, Avrupa gençlik etkinliklerinde, konferanslarda — yüz yüze, zaman içinde kurulan ilişkilerden gelir.</p>
      <blockquote>En iyi ortak, e-postanıza en hızlı yanıt veren kuruluş değildir. Zaten tanıdığınız, çalışmalarına saygı duyduğunuz, işler ters gittiğinde bile ortaya çıkacağına güvendiğiniz kuruluştur.</blockquote>
      <h2>Pratik Adımlar</h2>
      <ul>
        <li>Potansiyel ortaklarla ihtiyaç duymadan önce tanışmak için SALTO-YOUTH eğitim kurslarına ve Avrupa gençlik etkinliklerine katılın</li>
        <li>İlk iletişimde süreçte nerede olduğunuz konusunda dürüst olun — deneyimli kuruluşlar doğruluğu takdir eder</li>
        <li>Herhangi bir taahhütte bulunmadan önce görüntülü arama yapın — yazılı iletişim kişiliği ve çalışma kültürünü gizler</li>
        <li>Önceki proje işbirliklerinden referans isteyin</li>
        <li>Herhangi bir ortaklık anlaşmasını imzalamadan önce rolleri, sorumlulukları ve beklentileri yazılı olarak tanımlayın</li>
      </ul>
      <h2>YouthTICK Yaklaşımı</h2>
      <p>Şu anda ilk ortaklıklarımızı kurma sürecindeyiz. Bunu kasıtlı olarak yapıyoruz — dürüstlük, gençlik odaklı çalışma ve gerçek kültürlerarası diyalog konusundaki değerleri paylaşan kuruluşlara öncelik veriyoruz. Bunu okuyorsanız ve bu tanımda kuruluşunuzu tanıyorsanız, sizden haber almak isteriz.</p>
""",
'content_de': """
      <p>Internationale Partnerschaften für Erasmus+-Projekte aufzubauen ist einer der lohnendsten — und frustrierendsten — Teile der Jugendarbeit. Gut gemacht schafft es Beziehungen, die Jahre dauern, und Projekte, die das Leben der Teilnehmenden wirklich verändern. Schlecht gemacht verschwendet es Monate mit E-Mail-Austausch und führt zu einem Projekt, das vor der Einreichung auseinanderfällt.</p>
      <h2>Mit Werten beginnen, nicht mit Geografie</h2>
      <p>Der häufigste Fehler ist, den Partnerschaftsaufbau als logistische Übung zu behandeln. Sie brauchen einen Partner aus Deutschland (für die Förderregeln). Sie brauchen einen Partner, der gastgeben kann. Sie brauchen einen Partner, der die Finanzberichterstattung handhaben kann. All das stimmt — aber wenn Sie hier beginnen, landen Sie bei Organisationen, die technisch kompatibel, aber thematisch inkompatibel sind.</p>
      <p>Beginnen Sie mit: Worum geht es bei diesem Projekt wirklich? Welche Werte und Ansätze erfordert es? Wer arbeitet in anderen Ländern mit ähnlicher Energie und ähnlicher Integrität an diesen Fragen? Dann kümmern Sie sich um die Geografie.</p>
      <h2>Wo man wirklich Partner findet</h2>
      <p>Das SALTO Tool for Partnership (TCA) ist die umfassendste Datenbank, aber nicht der Ort, von dem die besten Partnerschaften stammen. Die besten Partnerschaften entstehen aus Beziehungen, die bei Trainingskursen, bei europäischen Jugendevents, bei Konferenzen aufgebaut wurden — persönlich, über Zeit.</p>
      <blockquote>Der beste Partner ist nicht die Organisation, die am schnellsten auf Ihre E-Mail antwortet. Es ist die Organisation, die Sie bereits kennen, deren Arbeit Sie respektieren, deren Team Sie vertrauen, dass es erscheint, auch wenn etwas schiefläuft.</blockquote>
      <h2>Praktische Schritte</h2>
      <ul>
        <li>Nehmen Sie an SALTO-YOUTH-Trainingskursen und europäischen Jugendveranstaltungen teil, um potenzielle Partner kennenzulernen, bevor Sie sie brauchen</li>
        <li>Seien Sie bei der ersten Kontaktaufnahme ehrlich darüber, wo Sie sich im Prozess befinden — erfahrene Organisationen schätzen Direktheit</li>
        <li>Führen Sie vor der Verpflichtung ein Videogespräch — schriftliche Kommunikation verbirgt Persönlichkeit und Arbeitskultur</li>
        <li>Bitten Sie um Referenzen aus früheren Projektzusammenarbeiten</li>
        <li>Definieren Sie Rollen, Verantwortlichkeiten und Erwartungen schriftlich, bevor Sie eine Partnerschaftsvereinbarung unterzeichnen</li>
      </ul>
      <h2>Der YouthTICK-Ansatz</h2>
      <p>Wir befinden uns derzeit im Prozess des Aufbaus unserer ersten Partnerschaften. Wir gehen dabei bewusst vor — wir priorisieren Organisationen, die unsere Werte rund um Ehrlichkeit, jugendzentrerte Arbeit und echten interkulturellen Dialog teilen. Wenn Sie das lesen und Ihre Organisation in dieser Beschreibung erkennen, würden wir gerne von Ihnen hören.</p>
"""
},
'7': {
'title_tr': "Fon Alan Güçlü Bir Erasmus+ KA1 Başvurusu Nasıl Yazılır",
'title_de': "Wie man einen starken Erasmus+ KA1-Antrag schreibt, der gefördert wird",
'content_tr': """
      <p>Her yıl Avrupa'daki binlerce gençlik kuruluşu Erasmus+ KA1 başvurusu yapıyor. Önemli bir bölümü reddediliyor — fikirler kötü olduğu için değil, başvurular değerlendiricilerin okumak için eğitildikleri dilde kalitelerini aktarmayı başaramadığı için. İşte fon alan başvuruları diğerlerinden ayıran şey.</p>
      <h2>KA1'in Gerçekte Neyi Ödüllendirdiğini Anlayın</h2>
      <p>KA1 — Bireylerin Öğrenme Hareketliliği — kuruluşların öğrenim amacıyla personel ve gençleri yurt dışına göndermesini finanse eder. Gençlik bileşeni kapsamında bu; gençlik değişimlerini, eğitim kurslarını ve gönüllülük faaliyetlerini içerir. Ancak anlaşılması gereken kilit nokta şudur: Erasmus+ deneyimleri değil, öğrenme çıktılarını finanse eder. Oturup yazmaya başladığınızda bu ayrım son derece önemlidir.</p>
      <p>Bir KA1 başvurusunun her bölümü aynı sorunun bir versiyonunu sorar: bu faaliyet gerçek, gösterilebilir, aktarılabilir bir öğrenmeye nasıl yol açıyor? Programınızın her unsuru için bunu açıkça yanıtlayamazsanız, faaliyet ne kadar ilgi çekici görünürse görünsün başvuru iyi puan almayacaktır.</p>
      <h2>İhtiyaç Değerlendirmesi: Çoğu Başvurunun Başarısız Olduğu Yer</h2>
      <p>İhtiyaç değerlendirmesi bölümü — kuruluşunuzun bu fona ve bu katılımcıların bu deneyime neden ihtiyaç duyduğunu açıklayan — tutarlı biçimde başarısız başvuruların en zayıf parçasıdır. Kuruluşlar belirsiz biçimde "gençleri güçlendirmek" veya "kapasite inşa etmek" istediklerini yazıyor. Değerlendiriciler somutluk istiyor.</p>
      <blockquote>Bir değerlendirici bir oturumda düzinelerce başvuru okur. Aklında kalanlar, belirli bir durumu o kadar net biçimde tarif edenlerdir ki faaliyetin gerekliliği açık — hatta kaçınılmaz — hale gelir.</blockquote>
      <h2>Öğrenme Hedefleri: Somut Olun</h2>
      <p>AKILLI hedefler kullanın. "Katılımcılar kültürlerarası yetkinlik geliştirecek" değil; "Katılımcılar, değişimden önce sahip oldukları ve deneyimin sorguladığı üç kültürel varsayımı tanımlayıp ifade edebilecek ve düşüncelerinin ya da davranışlarının nasıl değiştiğini açıklayabilecek." İkinci versiyon ölçülebilir. Birincisi değil.</p>
      <h2>Program: Metodolojinizi Gösterin</h2>
      <p>Yalnızca ne yapacağınızı değil, nasıl ve neden yapacağınızı açıklayın. Yaygın eğitim yöntemleri — balık kılçığı tartışmaları, dünya kafe, açık alan teknolojisi, forum tiyatrosu — adlandırılmalı ve kısaca açıklanmalıdır. Ekibinizin etkinlik düzenlemekten değil, öğrenmeyi kolaylaştırmaktan anladığını gösterin.</p>
      <h2>Bütçe: Gerçekçilik ve Şeffaflık</h2>
      <p>Bütçe bölümü rakamlardan çok güvenilirlikle ilgilidir. Gerçekçi olmayan maliyetler — çok düşük uçuş fiyatları, çok ucuz konaklama — deneyimsizliğe işaret eder. Olumsal düşünmeyi dahil edin. Araştırma yaptığınızı gösterin. Hibe yönetiminde yeniyseniz, mali kontrolleriniz hakkında dürüst olun ve sistemlerinizin mevcut olduğunu gösterin.</p>
      <h2>Bir Şey Daha</h2>
      <p>Program kılavuzunu okuyun. Tamamını. Her yıl güncelleniyor ve her yıl o yılın versiyonunda açıkça belirtilmiş bir şeyi kaçırdığı için başvurular reddediliyor. İki saat ayırın, dikkatlice okuyun ve başvurunuzu göndermeden önce bölüm bölüm karşılaştırın.</p>
""",
'content_de': """
      <p>Jedes Jahr reichen tausende von Jugendorganisationen in ganz Europa Erasmus+ KA1-Anträge ein. Ein erheblicher Teil wird abgelehnt — nicht weil die Ideen schlecht sind, sondern weil die Anträge ihre Qualität nicht in der Sprache kommunizieren, die Gutachter lesen können. Hier ist, was finanzierte Anträge von den anderen unterscheidet.</p>
      <h2>Verstehen, was KA1 wirklich belohnt</h2>
      <p>KA1 — Lernmobilität von Einzelpersonen — finanziert Organisationen, die Personal und junge Menschen zum Lernen ins Ausland schicken. Im Bereich Jugend umfasst dies Jugendbegegnungen, Trainingskurse und Freiwilligentätigkeiten. Aber das Entscheidende ist: Erasmus+ finanziert keine Erfahrungen. Es finanziert Lernergebnisse. Dieser Unterschied ist enorm wichtig, wenn man sich hinsetzt, um zu schreiben.</p>
      <p>Jeder Abschnitt eines KA1-Antrags stellt irgendeine Version derselben Frage: Wie führt diese Aktivität zu echtem, nachweisbarem, übertragbarem Lernen? Wenn man das für jedes Element des Programms nicht klar beantworten kann, wird der Antrag nicht gut bewertet — egal wie interessant die Aktivität klingt.</p>
      <h2>Die Bedarfsanalyse: Wo die meisten Anträge scheitern</h2>
      <p>Der Bedarfsanalyse-Abschnitt — der beschreibt, warum Ihre Organisation diese Förderung braucht und warum diese Teilnehmenden diese Erfahrung brauchen — ist durchgängig der schwächste Teil erfolgloser Anträge. Organisationen schreiben vage davon, junge Menschen „stärken" oder „Kapazitäten aufbauen" zu wollen. Gutachter brauchen Konkretes.</p>
      <blockquote>Ein Gutachter liest dutzende Anträge in einer Sitzung. Die, die haften bleiben, sind diejenigen, die eine spezifische Situation so klar beschreiben, dass die Notwendigkeit der Aktivität offensichtlich — ja sogar unvermeidlich — wird.</blockquote>
      <h2>Lernziele: Konkret sein</h2>
      <p>Verwenden Sie SMART-Ziele. Nicht „Teilnehmende werden interkulturelle Kompetenz entwickeln", sondern „Teilnehmende werden in der Lage sein, drei kulturelle Annahmen zu identifizieren und zu artikulieren, die sie vor dem Austausch hatten und die die Erfahrung herausgefordert hat, und zu beschreiben, wie sich ihr Verhalten oder Denken verändert hat." Die zweite Version ist bewertbar. Die erste nicht.</p>
      <h2>Das Programm: Ihre Methodik zeigen</h2>
      <p>Beschreiben Sie nicht nur was, sondern wie und warum. Non-formale Bildungsmethoden sollten benannt und kurz erklärt werden. Zeigen Sie, dass Ihr Team weiß, wie man Lernen facilitiert, nicht nur Veranstaltungen organisiert.</p>
      <h2>Budget: Realismus und Transparenz</h2>
      <p>Der Budgetabschnitt geht weniger um Zahlen als um Glaubwürdigkeit. Unrealistische Kosten signalisieren Unerfahrenheit. Zeigen Sie, dass Sie recherchiert haben. Wenn Sie neu im Fördermanagement sind, seien Sie ehrlich über Ihre finanziellen Kontrollen und zeigen Sie, dass Sie Systeme vorhanden haben.</p>
      <h2>Noch ein Hinweis</h2>
      <p>Lesen Sie den Programmleitfaden. Den ganzen. Jedes Jahr wird er aktualisiert, und jedes Jahr werden Anträge abgelehnt, weil ihnen etwas fehlt, das in der diesjährigen Version klar erläutert wurde. Nehmen Sie sich zwei Stunden, lesen Sie ihn sorgfältig und prüfen Sie Ihren Antrag Abschnitt für Abschnitt, bevor Sie ihn einreichen.</p>
"""
},
'8': {
'title_tr': "Yaygın Eğitim Nedir — ve Erasmus+ Neden Onun Üzerine İnşa Edilmiştir",
'title_de': "Was non-formale Bildung ist — und warum Erasmus+ darauf aufgebaut ist",
'content_tr': """
      <p>Erasmus+ çevrelerinde zaman geçirdiyseniz, "yaygın eğitim" teriminin sürekli kullanıldığını duymuşsunuzdur. Ama gerçekte ne anlama geliyor — ve Avrupa gençlik sektörü pratiğinin bu kadar büyük bir bölümünü neden onun üzerine kurmuştur?</p>
      <h2>Üç Öğrenme Türü</h2>
      <p>Standart çerçeve üç öğrenme türünü birbirinden ayırır. <strong>Örgün eğitim</strong> okullarda, üniversitelerde ve mesleki eğitim kurumlarında gerçekleşir — yapılandırılmış, müfredata dayalı ve tanınan niteliklere yol açar. <strong>Yaşam boyu öğrenme</strong> günlük yaşamda gerçekleşir: konuşmalar, medya, deneyim yoluyla bilgi edinme. <strong>Yaygın eğitim</strong> ikisi arasında yer alır: kasıtlı ve organize, ama resmi kurumlar dışında ve zorunlu olarak tanınan sertifikalara yol açmaz.</p>
      <p>Gençlik çalışması, toplum eğitimi, spor koçluğu, akran öğrenme programları ve Erasmus+ gençlik değişimleri hepsi yaygın eğitim kapsamına girer. Ortak özellikler paylaşırlar: gönüllü katılım, öğrenci merkezli tasarım, süreç ve sonuca odaklanma, önceki deneyimin tanınması.</p>
      <h2>Yaygın Yöntemler Neden Gençlik Çalışması İçin İşe Yarar</h2>
      <p>Örgün eğitim bilgi aktarmada ve bunun ne kadarının öğrenildiğini değerlendirmede mükemmeldir. Tutumları, değerleri, kimliği ve ilişkisel becerileri geliştirmede ise daha az etkilidir — tam da gençlik çalışmasının en çok önem verdiği şeyler bunlardır.</p>
      <blockquote>Kültürlerarası yetkinliği okuyarak öğrenmezsiniz. Dünya görüşü sizinkinden gerçekten farklı olan biriyle bir masanın karşısında oturarak, birlikte bir şeyi anlamaya çalışarak ve süreçte neler olduğunu fark ederek öğrenirsiniz.</blockquote>
      <h2>Kolb Döngüsü ve Gençlik Değişimleri</h2>
      <p>Çoğu yaygın eğitim pratiği David Kolb'un deneyimsel öğrenme döngüsüne dayanır: somut deneyim → yansıtıcı gözlem → soyut kavramsallaştırma → aktif deney. İyi yapılandırılmış bir gençlik değişimi katılımcıları tekrar tekrar bu dört aşamadan geçirir. Kötü yapılandırılmış bir gençlik değişimi ise sadece turizmdir.</p>
      <h2>Tanınma ve Doğrulama</h2>
      <p>Yaygın eğitimdeki kalıcı bir zorluk tanınmadır: öğrenmeyi işverenler, kurumlar ve toplum için nasıl görünür kılarsınız? Youthpass gibi araçların önemli hale geldiği yer burasıdır. AB ayrıca yaygın öğrenmeyi resmi sistemlerin anlayabileceği terimlerle ifade etmeye yardımcı olmak için Avrupa Beceri Pasaportu ve Europass gibi çerçeveler geliştirmiştir.</p>
""",
'content_de': """
      <p>Wenn Sie Zeit in Erasmus+-Kreisen verbracht haben, haben Sie den Begriff „non-formale Bildung" ständig gehört. Aber was bedeutet er eigentlich — und warum hat der europäische Jugendsektor so viel seiner Praxis darauf aufgebaut?</p>
      <h2>Drei Arten des Lernens</h2>
      <p>Der Standardrahmen unterscheidet drei Arten des Lernens. <strong>Formale Bildung</strong> findet in Schulen, Universitäten und Berufsbildungseinrichtungen statt — sie ist strukturiert, lehrplanbasiert und führt zu anerkannten Qualifikationen. <strong>Informelles Lernen</strong> findet im Alltag statt: Wissen durch Gespräche, Medien, Erfahrung aufnehmen. <strong>Non-formale Bildung</strong> liegt dazwischen: sie ist intentional und organisiert, findet aber außerhalb formaler Institutionen statt und führt nicht notwendigerweise zu anerkannten Abschlüssen.</p>
      <p>Jugendarbeit, Gemeinschaftsbildung, Sportcoaching, Peer-Learning-Programme und Erasmus+-Jugendbegegnungen fallen alle unter non-formale Bildung. Sie teilen gemeinsame Merkmale: freiwillige Teilnahme, lernerzentriertes Design, Fokus auf Prozess und Ergebnis, Anerkennung von Vorerfahrungen.</p>
      <h2>Warum non-formale Methoden in der Jugendarbeit funktionieren</h2>
      <p>Formale Bildung ist hervorragend darin, Wissen zu vermitteln und zu bewerten, ob es behalten wurde. Sie ist weniger effektiv darin, Einstellungen, Werte, Identität und relationale Fähigkeiten zu entwickeln — genau das, womit sich Jugendarbeit am meisten befasst.</p>
      <blockquote>Interkulturelle Kompetenz erlernt man nicht durch Lesen. Man erlernt sie, indem man jemandem gegenübersitzt, dessen Weltbild wirklich anders ist als das eigene, versucht, gemeinsam etwas zu verstehen, und bemerkt, was dabei passiert.</blockquote>
      <h2>Der Kolb-Zyklus und Jugendbegegnungen</h2>
      <p>Die meiste non-formale Bildungspraxis stützt sich auf David Kolbs Erfahrungslernen-Zyklus: konkrete Erfahrung → reflektive Beobachtung → abstrakte Konzeptualisierung → aktives Experimentieren. Eine gut strukturierte Jugendbegegnung führt Teilnehmende wiederholt durch alle vier Phasen. Eine schlecht strukturierte ist einfach Tourismus.</p>
      <h2>Anerkennung und Validierung</h2>
      <p>Eine anhaltende Herausforderung in der non-formalen Bildung ist die Anerkennung: Wie macht man das Lernen für Arbeitgeber, Institutionen und die Gesellschaft sichtbar? Hier werden Werkzeuge wie der Youthpass wichtig. Die EU hat auch Rahmen wie den Europäischen Kompetenzausweis und Europass entwickelt, um non-formales Lernen in Begriffe zu übersetzen, die formale Systeme verstehen können.</p>
"""
},
'9': {
'title_tr': "Youthpass: Erasmus+ Öğreniminizi Görünür Kılmak",
'title_de': "Der Youthpass: Erasmus+-Lernen sichtbar machen",
'content_tr': """
      <p>Youthpass, Erasmus+'ın kalıcı bir soruna verdiği yanıttır: yaygın öğrenmeyi nasıl okunabilir kılarsınız? Bir gencin sınav olmadan, not almadan ve resmi sertifika kazanmadan geçirdiği üç haftada gerçekte neler öğrendiğini gelecekteki bir işverene, üniversiteye veya toplum kuruluşuna nasıl gösterirsiniz?</p>
      <h2>Youthpass Nedir</h2>
      <p>Youthpass, Erasmus+ gençlik faaliyetlerine katılımcılara verilen bir sertifikadır. Faaliyeti, süresini ve — en önemlisi — katılımcının geliştirdiği yetkinlikleri, bizzat katılımcı tarafından yazılmış biçimde açıklar. Avrupa Gençlik Vakfı'nın sekiz temel yetkinlik çerçevesine bağlıdır; çok dilli yetkinlik, dijital okuryazarlık, kişisel ve sosyal yetkinlik, sivil yetkinlik ve girişimcilik gibi alanları kapsar.</p>
      <p>Sertifika çevrimiçi bir platform (youthpass.eu) aracılığıyla oluşturulur ve ücretsizdir. AB üye devletleri genelinde resmi olarak tanınır, ancak işverenler ve kurumlar arasında pratikte tanınma düzeyi önemli ölçüde değişmektedir.</p>
      <h2>Süreç: Belgeden Daha Önemli</h2>
      <p>Birçok kişinin Youthpass hakkında gözden kaçırdığı şey, belgenin sürecin neredeyse ikincil planda kaldığıdır. Youthpass, yapılandırılmış öz-yansıma yoluyla geliştirilmek üzere tasarlanmıştır — sonunda değil, faaliyet sırasında başlayan bir süreç.</p>
      <blockquote>Youthpass'ın en değerli kısmı indirebileceğiniz sertifika değildir. Kendinize sorarken geçirdiğiniz saattir: Gerçekte ne öğrendim? Şimdi önceden yapamadığım ne yapabiliyorum? Düşüncelerim nasıl değişti?</blockquote>
      <h2>Nasıl Kullanılır</h2>
      <p>Erasmus+ faaliyetini tamamlayan katılımcılar Youthpass'larını Europass portföylerine eklemelidir. Listeledikleri her yetkinlik hakkında konuşabilmeliler — programdan somut örneklerle. İyi hazırlanmış bir katılımcı, "demokratik katılıma odaklanan on günlük bir gençlik değişiminde sivil yetkinliğimi geliştirdim" cümlesini liderlik, ekip çalışması veya farklılıklar üzerinden çalışma hakkındaki bir mülakat sorusuna ikna edici bir yanıta dönüştürebilir.</p>
""",
'content_de': """
      <p>Der Youthpass ist Erasmus+' Antwort auf ein dauerhaftes Problem: Wie macht man non-formales Lernen lesbar? Wie hilft man einem jungen Menschen zu zeigen, was er während drei Wochen in einem anderen Land wirklich gelernt hat — wenn es keine Prüfung, keine Note und kein formales Zertifikat gab?</p>
      <h2>Was der Youthpass ist</h2>
      <p>Der Youthpass ist ein Zertifikat, das Teilnehmenden an Erasmus+-Jugendaktivitäten ausgestellt wird. Es beschreibt die Aktivität, die Dauer und — am wichtigsten — die Kompetenzen, die der Teilnehmende entwickelt hat, geschrieben von dem Teilnehmenden selbst. Es ist mit dem Rahmen der acht Schlüsselkompetenzen der Europäischen Jugendstiftung verknüpft, der Bereiche wie mehrsprachige Kompetenz, digitale Kompetenz, persönliche und soziale Kompetenz, Bürgerkompetenz und Unternehmertum umfasst.</p>
      <p>Das Zertifikat wird über eine Online-Plattform (youthpass.eu) erstellt und ist kostenlos. Es wird in allen EU-Mitgliedstaaten offiziell anerkannt, obwohl die Anerkennung in der Praxis zwischen Arbeitgebern und Institutionen erheblich variiert.</p>
      <h2>Der Prozess: Wichtiger als das Dokument</h2>
      <p>Was viele über den Youthpass übersehen, ist, dass das Dokument fast zweitrangig gegenüber dem Prozess seiner Erstellung ist. Der Youthpass soll durch strukturierte Selbstreflexion entwickelt werden — ein Prozess, der während der Aktivität beginnt, nicht am Ende.</p>
      <blockquote>Der wertvollste Teil des Youthpass ist nicht das Zertifikat, das Sie herunterladen können. Es ist die Stunde, die Sie damit verbringen, sich selbst zu fragen: Was habe ich wirklich gelernt? Was kann ich jetzt, was ich vorher nicht konnte? Wie hat sich mein Denken verändert?</blockquote>
      <h2>Wie man ihn nutzt</h2>
      <p>Teilnehmende, die eine Erasmus+-Aktivität abgeschlossen haben, sollten ihren Youthpass in ihr Europass-Portfolio aufnehmen. Sie sollten über jede aufgeführte Kompetenz sprechen können — mit einem konkreten Beispiel aus dem Programm. Ein gut vorbereiteter Teilnehmender kann „Ich habe meine Bürgerkompetenz während eines zehntägigen Jugendaustauschs zu demokratischer Partizipation entwickelt" in eine überzeugende Antwort auf eine Interviewfrage über Führung, Teamarbeit oder das Arbeiten über Unterschiede hinweg verwandeln.</p>
"""
},
'10': {
'title_tr': "Erasmus+ KA2'yi Anlamak: STK'lar İçin İşbirliği Projeleri",
'title_de': "Erasmus+ KA2 verstehen: Kooperationsprojekte für NGOs",
'content_tr': """
      <p>KA1 Erasmus+'ın hareketlilik bileşeniyse — insanların seyahat edip öğrenmesini finanse ediyorsa — KA2 de onun inovasyon bileşenidir. İşbirliği Projeleri, birden fazla ülkeden kuruluşları yeni bir şey geliştirmek için bir araya getirir: müfredat, metodoloji, araç, politika önerisi. Yönetmesi daha karmaşık ve kazanması daha zordur, ama onlarla ilgilenmeye hazır kuruluşlar için dönüştürücüdür.</p>
      <h2>KA2 Neyi Finanse Eder</h2>
      <p>Gençlik bileşeni kapsamında KA2; "İşbirliği Ortaklıkları" ve "Küçük Ölçekli Ortaklıklar"ı finanse eder. İşbirliği Ortaklıkları büyük formattır — genellikle üç ila dört yıl, en az üç ülkeden birden fazla ortak, önemli bütçeler (60.000–500.000 € veya daha fazla). Küçük Ölçekli Ortaklıklar daha erişilebilir olmak üzere tasarlanmıştır: daha kısa (12–24 ay), daha az ortak (en az iki ülke), daha küçük bütçeler (10.000–60.000 €).</p>
      <blockquote>En güçlü KA2 projeleri, bir kuruluşun işi yaptığı ve diğerlerinin logo sağladığı projeler değildir. Bunlar, her ortağın bağlamının çıktıları gerçekten şekillendirdiği — son ürünün herkes odada olmadan var olamayacağı projelerdir.</blockquote>
      <h2>Güçlü Bir KA2 Başvurusu Neyi Gerektirir</h2>
      <p>KA2 başvuruları, tüm Erasmus+ başvurularına uygulanan gereksinimlerin (açık ihtiyaç değerlendirmesi, AKILLI hedefler, değerlendirme planı) ötesinde ek bir şey göstermek zorundadır: konsorsiyumun gerçek anlamda tamamlayıcı uzmanlık getirdiğini ve proje tasarımının bu uzmanlığı stratejik olarak kullandığını.</p>
      <h2>KA2 Kuruluşunuz İçin Doğru mu?</h2>
      <p>KA2 önemli ölçüde yönetim kapasitesi gerektirir. Raporlama, mali yönetim ve koordinasyon yükü önemlidir — özellikle büyük İşbirliği Ortaklıklarında. Avrupa hibelerini yönetme deneyimi olmayan kuruluşlar için Küçük Ölçekli Ortaklık formatı daha uygun bir başlangıç noktasıdır.</p>
      <p>YouthTICK olarak gelecekteki KA2 olasılıklarını araştırıyoruz. Kuruluşunuz gençlik alanında ortak bir proje geliştirmeyle ilgileniyorsa, konuşmayı memnuniyetle karşılarız.</p>
""",
'content_de': """
      <p>Wenn KA1 der Mobilitätsstrang von Erasmus+ ist — Menschen zum Reisen und Lernen zu finanzieren — dann ist KA2 sein Innovationsstrang. Kooperationsprojekte bringen Organisationen aus mehreren Ländern zusammen, um etwas Neues zu entwickeln: einen Lehrplan, eine Methodik, ein Werkzeug, eine Politikempfehlung. Sie sind komplexer zu managen und schwerer zu gewinnen, aber für Organisationen, die bereit sind, sich damit auseinanderzusetzen, sind sie transformativ.</p>
      <h2>Was KA2 finanziert</h2>
      <p>Im Bereich Jugend finanziert KA2 „Kooperationspartnerschaften" und „Kleinpartnerschaften". Kooperationspartnerschaften sind das größere Format — typischerweise drei bis vier Jahre, mehrere Partner aus mindestens drei Ländern, erhebliche Budgets (60.000–500.000 € oder mehr). Kleinpartnerschaften sind zugänglicher konzipiert: kürzer (12–24 Monate), weniger Partner (mindestens zwei Länder), kleinere Budgets (10.000–60.000 €).</p>
      <blockquote>Die mächtigsten KA2-Projekte sind nicht die, bei denen eine Organisation die Arbeit erledigt und andere ein Logo liefern. Es sind die, bei denen der Kontext jedes Partners die Ergebnisse wirklich prägt — wo das Endprodukt ohne alle im Raum nicht hätte existieren können.</blockquote>
      <h2>Was einen starken KA2-Antrag ausmacht</h2>
      <p>Über die Anforderungen, die für alle Erasmus+-Anträge gelten hinaus (klare Bedarfsanalyse, SMART-Ziele, Evaluierungsplan), müssen KA2-Anträge etwas Zusätzliches demonstrieren: dass das Konsortium wirklich komplementäre Expertise mitbringt und dass das Projektdesign diese Expertise strategisch nutzt.</p>
      <h2>Ist KA2 das Richtige für Ihre Organisation?</h2>
      <p>KA2 erfordert erhebliche Managementkapazität. Die Berichts-, Finanzmanagement- und Koordinationsbelastung ist erheblich. Für Organisationen ohne Erfahrung im Management europäischer Fördermittel ist das Kleinpartnerschaftsformat ein geeigneterer Ausgangspunkt.</p>
      <p>Bei YouthTICK erkunden wir zukünftige KA2-Möglichkeiten. Wenn Ihre Organisation daran interessiert ist, gemeinsam ein Projekt im Jugendbereich zu entwickeln, würden wir das Gespräch begrüßen.</p>
"""
},
}

def add_translations(filepath, trans_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for art_id, trans in trans_dict.items():
        # Build the insertion string
        insert = ""
        for key, val in trans.items():
            # Escape backticks inside the content
            safe_val = val.replace('`', "'")
            insert += f",\n    {key}: `{safe_val}`"

        # Find the article block and insert before its closing brace
        # Pattern: find '  'ID': {' ... content: `...`\n  }
        # We look for the content field of this article and insert after it
        pattern = rf"(  '{art_id}': {{.*?content: `.*?`)"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            end = match.end()
            # Make sure we're not already translated
            after = content[end:end+200]
            if f'content_tr' not in content[end-50:end+50]:
                content = content[:end] + insert + content[end:]
                print(f"  ✓ Article {art_id} translated")
        else:
            print(f"  ✗ Article {art_id} not found")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nDone. Wrote {filepath}")

if __name__ == '__main__':
    import os
    filepath = os.path.join(os.path.dirname(__file__), 'assets', 'js', 'data', 'articles.js')
    add_translations(filepath, TRANS)
