#!/usr/bin/env python3
"""Add TR + DE translations for articles 24-35."""
import re, sys

path = "assets/js/data/articles.js"
with open(path, encoding="utf-8") as f:
    content = f.read()

translations = {
    '24': {
        'title_tr': 'Gerçekten İşleyen Gençlik Konseyleri: Avrupa Genelinden Dersler',
        'title_de': 'Jugendräte, die wirklich funktionieren: Lehren aus ganz Europa',
        'content_tr': """
      <p>Gençlik konseyleri — gençlerin yerel veya ulusal yönetişime katıldığı resmi organlar — neredeyse her Avrupa ülkesinde mevcuttur. Bunların büyük çoğunluğu işe yaramamaktadır. Sembolik kalmakta, yetersiz kaynaklara sahip olmakta, yetişkin gündemleri tarafından domine edilmekte ve hızla hayal kırıklığına uğrayıp ayrılan dar bir demografiye hitap etmektedir. Ama bazıları gerçekten işe yarar. Ve işe yarayanların ortak, tanımlanabilir özellikleri vardır.</p>
      <h2>Sembolizm Sorunu</h2>
      <p>En yaygın başarısızlık biçimi sembolizmdir: bir gençlik konseyi var, düzenli toplantı yapıyor, üyeleri rapor yazıyor ve etkinliklere katılıyor — ama söyledikleri hiçbir şeyin kararlar üzerinde gerçek bir etkisi yok. Kurumdaki yetişkinler kibarca dinliyor ve sonra zaten yapacakları şeyi yapıyor. Gençler sürece dahil ediliyor ama güçten dışlanıyor.</p>
      <p>Sherry Arnstein'ın 1969'da geliştirilen ama hâlâ çarpıcı biçimde doğru olan Vatandaş Katılımı Merdiveni, manipülasyondan (alt basamak) vatandaş kontrolüne (üst basamak) kadar sekiz seviye tanımlamaktadır. Çoğu gençlik konseyi "danışmanlık" etrafında bir yerlerde faaliyet gösterir — beşinci veya altıncı basamak — ve gençler gerçek katılım ile katılımın yönetilen performansı arasındaki farkı ayırt edebilir.</p>
      <h2>Etkili Gençlik Konseylerinin Ortak Özellikleri</h2>
      <p>İskandinav belediye gençlik konseylerinden Almanya ve İngiltere'deki ulusal gençlik parlamentolarına kadar Avrupa bağlamlarındaki araştırmalar, gerçekten karar etkileyen gençlik konseylerinin birkaç tutarlı özelliğini ortaya koymaktadır:</p>
      <ul>
        <li><strong>Gerçek yetki</strong>: yalnızca danışmanlık statüsüyle değil, gerçek karar alma yetkisine sahip olduğu açıkça tanımlanmış bir alan</li>
        <li><strong>Özel bütçe</strong>: gençlerin kendi önceliklerine göre tahsis edebileceği anlamlı kaynaklar üzerinde kontrol — küçük olsa bile</li>
        <li><strong>Doğrudan erişim</strong>: gençlik çalışanları veya program yöneticileri aracılığıyla filtrelenmeden karar vericilere düzenli ve yapılandırılmış erişim</li>
        <li><strong>Yeterli destek</strong>: süreci kontrol etmeden destekleyen eğitimli yetişkin kolaylaştırıcılar ve pratik işler için idari destek</li>
        <li><strong>Çeşitli üyelik</strong>: gönüllü olarak öne çıkanlara değil, sivil açıdan henüz meşgul olmayan gençlere aktif erişim</li>
      </ul>
      <blockquote>İşleyen gençlik konseyi, en iyi gençlere sahip olan değil — gençlerin gerçek etki kullanmasını mümkün kılan kurumsal yapıya sahip olandır. Yapı, bireylerden daha önemlidir.</blockquote>
      <h2>Yalova Bağlamı</h2>
      <p>Türk belediyeleri son on yılda giderek artan biçimde gençlik katılım yapılarını denemiştir. Kalite büyük farklılıklar göstermektedir. En iyi örnekler — ilgili belediye liderliğine sahip büyük şehirlerde — kentsel tasarımdan kültürel programlamaya kadar birçok konuda gençlerin yerel politikayı şekillendirmesi için gerçek alan yaratmıştır. En kötüleri ise büyük ölçüde törenseldir.</p>
      <p>YouthTICK olarak Yalova bağlamında anlamlı gençlik katılımının nasıl görüneceğini araştırıyoruz — başka bir yerden model ithal etmek yerine yerel ilişkilere, ihtiyaçlara ve olanaklara kök salmış bir model geliştiriyoruz. Bunun parçası olmak isteyen bir Yalova genci iseniz, bize ulaşın.</p>
    """,
        'content_de': """
      <p>Jugendräte — formelle Gremien, durch die junge Menschen an der lokalen oder nationalen Regierungsführung teilnehmen — existieren in fast jedem europäischen Land. Die meisten von ihnen funktionieren nicht. Sie sind symbolisch, schlecht ausgestattet, von Erwachsenenagenden dominiert und werden von einer kleinen demografischen Gruppe bereits engagierter junger Menschen besucht, die schnell desillusioniert werden und gehen. Aber einige funktionieren tatsächlich. Und diejenigen, die funktionieren, haben identifizierbare gemeinsame Merkmale.</p>
      <h2>Das Tokenismus-Problem</h2>
      <p>Der häufigste Versagensmodus ist Tokenismus: Ein Jugendrat existiert, trifft sich regelmäßig, seine Mitglieder schreiben Berichte und nehmen an Veranstaltungen teil — aber nichts, was sie sagen, hat irgendeinen echten Einfluss auf Entscheidungen. Erwachsene in der Institution hören höflich zu und machen dann das, was sie sowieso getan hätten. Die jungen Menschen werden in den Prozess einbezogen, aber von der Macht ausgeschlossen.</p>
      <p>Sherry Arnsteins Leiter der Bürgerbeteiligung — entwickelt 1969, aber immer noch erschreckend genau — beschreibt acht Ebenen von Manipulation (unten) bis zur Bürgerkontrolle (oben). Die meisten Jugendräte operieren irgendwo um „Konsultation" herum — Sprosse fünf oder sechs — und junge Menschen können den Unterschied zwischen echtem Engagement und inszeniertem Engagement erkennen.</p>
      <h2>Was effektive Jugendräte gemeinsam haben</h2>
      <p>Forschungen in europäischen Kontexten — von skandinavischen kommunalen Jugendräten bis hin zu nationalen Jugendparlamenten in Deutschland und dem Vereinigten Königreich — identifizieren mehrere konsistente Merkmale von Jugendräten, die tatsächlich Entscheidungen beeinflussen:</p>
      <ul>
        <li><strong>Echtes Mandat</strong>: ein klar definierter Bereich, in dem der Rat echte Entscheidungsbefugnis hat, nicht nur Beratungsstatus</li>
        <li><strong>Eigenes Budget</strong>: Kontrolle über bedeutungsvolle Ressourcen — auch kleine —, die junge Menschen nach ihren eigenen Prioritäten zuteilen können</li>
        <li><strong>Direkter Zugang</strong>: regelmäßiger, strukturierter Zugang zu Entscheidungsträgern — nicht durch Jugendarbeiter oder Programmbeauftragte gefiltert</li>
        <li><strong>Ausreichende Unterstützung</strong>: geschulte erwachsene Moderatoren, die den Prozess unterstützen ohne ihn zu kontrollieren, und administrative Unterstützung für die Praktisches</li>
        <li><strong>Vielfältige Mitgliedschaft</strong>: aktive Kontaktaufnahme mit jungen Menschen, die nicht bereits zivilgesellschaftlich engagiert sind</li>
      </ul>
      <blockquote>Der Jugendrat, der funktioniert, ist nicht derjenige mit den besten jungen Menschen — es ist derjenige mit der institutionellen Struktur, die es jungen Menschen ermöglicht, echten Einfluss auszuüben. Die Struktur ist wichtiger als die Individuen.</blockquote>
      <h2>Der Yalova-Kontext</h2>
      <p>Türkische Kommunen haben im vergangenen Jahrzehnt zunehmend mit Strukturen zur Jugendbeteiligung experimentiert. Die Qualität variiert enorm. Bei YouthTICK erkunden wir, wie bedeutungsvolle Jugendbeteiligung im Yalova-Kontext aussieht — nicht ein Modell von anderswo importieren, sondern eines entwickeln, das in lokalen Beziehungen, Bedürfnissen und Möglichkeiten verwurzelt ist.</p>
    """
    },
    '25': {
        'title_tr': 'Anlamlı Bir Gençlik İstişare Süreci Nasıl Yürütülür',
        'title_de': 'Wie man einen bedeutungsvollen Jugendbeteiligungsprozess durchführt',
        'content_tr': """
      <p>Gençlik istişaresi bir güvenilirlik sorunuyla karşı karşıyadır. Gençler yeterince "istişare edildi" — çevrimiçi anketler, sembolik odak grupları ve sahnelenmiş etkinlikler aracılığıyla — alınan kararlar için meşruiyet üretmeye mi, yoksa henüz alınmamış kararları gerçekten bilgilendirmeye mi yönelik bir süreçle karşılaştıklarını ayırt edecek kadar deneyim kazandı. Anlamlı bir istişare yürütmek bu güvenilirlik açığını doğrudan ele almayı gerektirir.</p>
      <h2>Sonuçlarla Gerçekten Ne Yapacağınızı Belirleyin</h2>
      <p>Herkese danışmadan önce şunu netleştirin — dahili olarak ve kamuoyuna açık biçimde: bu istişare hangi kararları bilgilendirecek? Olası sonuçların yelpazesi nedir? Farklı istişare bulgularının sonucunda gerçekten ne değişirdi? Eğer yanıtlar belirsizse ya da sonuç yelpazesi dardır, meşruiyet alıştırması yürütüyor olabilirsiniz. Kısıtlamaların dürüstçe kabul edilmesi, sahte açıklıktan her zaman daha iyidir.</p>
      <p>Bunu gençlere baştan açıkça bildirin. Karar alma sürecini gösterin. Katkılarının nerede devreye gireceğini açıklayın. Zaman çizelgesi hakkında somut olun. Ve ardından — en önemlisi — geri bildirin. Katılımlarının sonucunda neyin değiştiğini gençlere gösterin ve diğer şeylerin neden değişmediğini dürüstçe açıklayın.</p>
      <h2>Olağan Şüphelilerin Ötesine Geçin</h2>
      <p>Çoğu gençlik istişaresindeki en büyük tasarım hatası örneklem yanlılığıdır. Açık istişare süreçlerine yanıt veren gençler zaten meşguldür: katılmak için özgüven, bilgi ve zamana sahiptirler. En çok ihtiyaç duyulan sesler — alınan kararlardan en çok etkilenenler, resmi süreçlere en yabancılaşmışlar — katılmaya en az ilgi gösterenlerdir.</p>
      <blockquote>İstişare bulgularınız önceden inandıklarınızı onaylıyorsa örnekleminizi kontrol edin. Ya başından beri haklıydınız — mümkün — ya da yalnızca sizinle zaten aynı fikirde olan kişilerden duyuyorsunuzdur.</blockquote>
      <p>Olağan şüphelilerin ötesine geçmek, aktif erişim, güvenilir aracılar, gençlere sizin için uygun olan yerde değil bulundukları yerde ulaşmak ve zaten sivil açıdan meşgul olmayan kişiler için erişilebilir ve çekici biçimlerde katılım sunmayı gerektirir.</p>
      <h2>Amaca Uygun Yöntemler Seçin</h2>
      <ul>
        <li><strong>Çevrimiçi anketler</strong>: hızlı, ucuz, ölçeklenebilir — ama yüzeysel. Tercihler hakkında nicel veri için iyi, ancak nedenler veya karmaşıklığı anlamak için değil</li>
        <li><strong>Odak grupları</strong>: daha zengin veri, ancak grup dinamiklerine ve kolaylaştırıcı etkisine karşı savunmasız. Dikkatli tasarım ve yönlendirme gerektirir</li>
        <li><strong>Dünya Kafeleri ve Açık Alan</strong>: katılımcıların gündemi belirlemesine izin verir — sorunların ne olduğunu bilmediğinizde keşif amaçlı istişareler için iyi</li>
        <li><strong>Katılımcı Eylem Araştırması</strong>: gençler özne değil araştırmacı olarak. Zaman yoğun ama en gerçek içgörüleri üretir</li>
        <li><strong>Dijital katılım platformları</strong>: Decidim veya Consul gibi araçlar, ölçekte eşzamansız demokratik katılıma olanak sağlar</li>
      </ul>
      <h2>İstişareden Sonra</h2>
      <p>En önemli aşama verileri topladıktan sonra gerçekleşir. Dürüstçe analiz edin — varsayımlarınıza meydan okuyan bulgular dahil. Gençlerin anlayabileceği ve paylaşabileceği sade bir özet yazın. Yayınlayın. Katılımcılara ne kararlaştırıldığını ve neden kararlaştırıldığını geri bildirin. İnsanlara yalnızca zamanları için değil, katkılarının önemli olduğunu göstererek teşekkür edin. Sessizlikte biten bir istişare süreci, hiç istişare yapmamaktan daha kötüdür.</p>
    """,
        'content_de': """
      <p>Jugendbeteiligung hat ein Glaubwürdigkeitsproblem. Junge Menschen wurden oft genug „konsultiert" — durch Online-Umfragen, symbolische Fokusgruppen und inszenierte Veranstaltungen —, um zu erkennen, wann ein Prozess darauf ausgelegt ist, Legitimität für bereits getroffene Entscheidungen zu erzeugen, anstatt noch zu treffende Entscheidungen wirklich zu informieren. Eine bedeutungsvolle Konsultation durchzuführen erfordert, diese Glaubwürdigkeitslücke direkt anzugehen.</p>
      <h2>Definieren Sie, was Sie mit den Ergebnissen tatsächlich tun werden</h2>
      <p>Bevor Sie irgendjemanden konsultieren, klären Sie — intern und öffentlich —: Welche Entscheidungen soll diese Konsultation informieren? Was ist die Bandbreite möglicher Ergebnisse? Was würde sich bei unterschiedlichen Konsu­ltationsergebnissen wirklich ändern? Wenn die Antworten vage sind oder die Bandbreite der Ergebnisse eng ist, führen Sie möglicherweise eine Legitimationsübung durch. Ehrliches Eingestehen von Einschränkungen ist immer besser als falsche Offenheit.</p>
      <p>Kommunizieren Sie dies klar an junge Menschen von Anfang an. Zeigen Sie ihnen den Entscheidungsprozess. Erklären Sie, wo ihr Beitrag einfließen wird. Seien Sie konkret über den Zeitplan. Und dann — entscheidend — berichten Sie zurück, was passiert ist.</p>
      <h2>Über die üblichen Verdächtigen hinausgehen</h2>
      <p>Der größte Designfehler in den meisten Jugendbeteiligungsprozessen ist die Stichprobenverzerrung. Die jungen Menschen, die auf offene Beteiligungsprozesse reagieren, sind bereits engagiert. Die jungen Menschen, deren Stimmen am meisten gebraucht werden, kommen am wenigsten.</p>
      <blockquote>Wenn Ihre Konsultationsergebnisse bestätigen, was Sie bereits geglaubt haben, überprüfen Sie Ihre Stichprobe. Entweder hatten Sie von Anfang an recht — möglich — oder Sie haben nur von Menschen gehört, die bereits mit Ihnen übereinstimmten.</blockquote>
      <h2>Methoden wählen, die dem Zweck entsprechen</h2>
      <ul>
        <li><strong>Online-Umfragen</strong>: schnell, günstig, skalierbar — aber oberflächlich</li>
        <li><strong>Fokusgruppen</strong>: reichhaltigere Daten, aber anfällig für Gruppendynamiken</li>
        <li><strong>World Cafés und Open Space</strong>: ermöglichen es Teilnehmern, die Agenda zu gestalten</li>
        <li><strong>Partizipative Aktionsforschung</strong>: junge Menschen als Mitforscher, nicht nur als Subjekte</li>
        <li><strong>Digitale Beteiligungsplattformen</strong>: Tools wie Decidim oder Consul ermöglichen asynchrone, demokratische Teilhabe</li>
      </ul>
      <h2>Nach der Konsultation</h2>
      <p>Die wichtigste Phase ist die, die nach der Datenerhebung stattfindet. Analysieren Sie ehrlich — einschließlich der Ergebnisse, die Ihre Annahmen in Frage stellen. Schreiben Sie eine verständliche Zusammenfassung. Veröffentlichen Sie sie. Berichten Sie den Teilnehmern, was entschieden wurde und warum. Ein Konsultationsprozess, der im Schweigen endet, ist schlimmer als gar keine Konsultation.</p>
    """
    },
    '26': {
        'title_tr': 'Yerel Demokrasi ve Gençler: Katılım İçin Rehber',
        'title_de': 'Lokale Demokratie und junge Menschen: Ein Leitfaden zur Beteiligung',
        'content_tr': """
      <p>Günlük yaşamı gerçekten etkileyen kararların büyük çoğunluğu yerel yönetimlerde alınır. Ulaşım, konut, parklar, gençlik hizmetleri, kültürel tesisler, yerel planlama — bunlar teoride yerel sakinlere karşı sorumlu olan yerel meclis üyeleri ve yöneticiler tarafından belediye düzeyinde belirlenir. Gençler yerel sakinlerdir. Ve yerel demokrasi, anlamlı sivil katılıma en erişilebilir giriş noktalarından biridir.</p>
      <h2>Neden Yerel? Neden Ulusal Değil?</h2>
      <p>Ulusal siyaset uzak, karmaşık ve çoğu zaman teatral hissettiriyor. Bir gencin günlük kaygıları ile ulusal parlamentodaki tartışmalar arasındaki mesafe aşılmaz görünebilir. Yerel siyaset farklıdır. Karar verenler çoğu zaman ulaşılabilirdir — meclis toplantılarında, topluluk etkinliklerinde, yerel kafede. Konular somut ve görünürdür. Eylem ile sonuç arasındaki süre on yıllarla değil aylarla ölçülür.</p>
      <p>Sivil katılım araştırmaları tutarlı biçimde şunu gösterir: yerel siyasette aktif hale gelen kişilerin zaman içinde sivil katılımı sürdürme olasılığı önemli ölçüde daha yüksektir. Yerel katılım, daha geniş katılımı mümkün kılan özgüveni, bilgiyi ve ağları oluşturur. Bu daha az bir demokrasi biçimi değil — genellikle en etkili giriş noktasıdır.</p>
      <h2>Yerel Yönetim Nasıl İşler?</h2>
      <p>Çoğu genç yerel yönetimin nasıl işlediği hakkında hiçbir fikre sahip değildir — ki bu şaşırtıcı değil, zira nadiren öğretilir. Temelleri anlamak katılımın ilk adımıdır. Türk belediyelerinde temel yapılar şunlardır: Belediye Meclisi (seçilmiş, politika belirler), Belediye Başkanı (yürütme yetkisi) ve hizmet sunan çeşitli müdürlükler.</p>
      <p>Çoğu karar öngörülebilir bir süreçten geçer: teklif → komisyon incelemesi → meclis oyu → uygulama. Bunların büyük çoğunluğu kamuya açık olarak kayıt altına alınır ve prensipte komisyon aşamasında kamuoyunun katılımına açıktır. Çok az kişi bu avantajdan yararlanır. Gençler — düzenli olarak gelen, halk katılım bölümünde konuşan, yazılı temsil sunan — genellikle salondaki tek sivil olurlar. Bu onlara orantısız bir görünürlük sağlar.</p>
      <blockquote>On beş halk üyesiyle gerçekleşen belediye meclisi toplantısı nadir ve güçlü bir şeydir. Tutarlı biçimde gelen, net konuşan ve yazılı takip yapan genç hatırlanır. Yerel demokrasi, ulusal siyasetten daha fazla bireysel etki alanı sunar — tam da çok az kişi kullandığı için.</blockquote>
      <h2>Pratik Giriş Noktaları</h2>
      <ul>
        <li><strong>Bir meclis toplantısına katılın</strong>: çoğu toplantı halka açık ve ücretsizdir. Gündemi önceden çevrimiçi bulun — belirli bir konuyla gelin</li>
        <li><strong>Yerel meclis üyenizle iletişime geçin</strong>: sizi etkileyen bir konuda somut, özlü bir mektup veya e-posta yazın. Takip edin</li>
        <li><strong>Bir istişare sürecine katılın</strong>: yerel yönetimler planlama, hizmetler ve bütçeler hakkında istişareler düzenler — çoğunlukla minimal katılımla. Gidin</li>
        <li><strong>Bir topluluk derneğine katılın</strong>: mahalle dernekleri, spor kulüpleri ve kültürel örgütler yerel demokrasinin taban altyapısıdır</li>
        <li><strong>Bir şeyler başlatın</strong>: topluluk bahçesi, gençlik etkinliği, mahalle temizliği — yerel yönetimler genellikle topluluk katılımını gösteren girişimleri desteklemeye hazırdır</li>
      </ul>
      <h2>Uzun Vadeli İnşa</h2>
      <p>Yerel demokratik katılım en çok sürdürüldüğünde etkilidir. Bir meclis toplantısında tek bir görünüm hiçbir şeyi değiştirmez. Tutarlı varlık, zaman içinde ilişki kurma ve güvenilirlik ile bilginin birikmesi — gerçek etki için koşullar bunları yaratır.</p>
    """,
        'content_de': """
      <p>Die Kommunalverwaltung ist dort, wo die meisten Entscheidungen getroffen werden, die das tägliche Leben tatsächlich beeinflussen. Transport, Wohnen, Parks, Jugendangebote, Kultureinrichtungen, lokale Planung — diese werden auf kommunaler Ebene von Gemeinderäten und Verwaltungsbeamten bestimmt, die theoretisch gegenüber den Einwohnern verantwortlich sind. Junge Menschen sind Einwohner. Und die Lokalpolitik ist einer der zugänglichsten Einstiegspunkte für bedeutungsvolle Bürgerbeteiligung.</p>
      <h2>Warum lokal? Warum nicht national?</h2>
      <p>Die nationale Politik fühlt sich distant, komplex und oft theatralisch an. Die lokale Politik ist anders. Die Entscheidungsträger sind oft erreichbar — bei Ratssitzungen, Gemeinschaftsveranstaltungen, im lokalen Café. Die Themen sind konkret und sichtbar. Und die Zeit zwischen Aktion und Ergebnis ist in Monaten, nicht in Jahrzehnten messbar.</p>
      <h2>Wie Kommunalverwaltung wirklich funktioniert</h2>
      <p>Die meisten Entscheidungen durchlaufen einen vorhersehbaren Prozess: Antrag → Ausschussprüfung → Ratsbeschluss → Umsetzung. Vieles davon ist öffentlich protokolliert und steht im Prinzip dem öffentlichen Engagement offen. Nur sehr wenige Menschen nutzen dies. Junge Menschen, die erscheinen, die im Abschnitt für öffentliche Beteiligung sprechen, die schriftliche Eingaben machen, sind oft die einzigen Nicht-Beamten im Raum.</p>
      <blockquote>Die Gemeinderatssitzung mit fünfzehn Mitgliedern der Öffentlichkeit ist eine seltene und mächtige Sache. Der junge Mensch, der konsistent erscheint, klar spricht und schriftlich nachfasst, wird erinnert. Die Lokalpolitik hat mehr Raum für individuellen Einfluss als die nationale Politik — genau weil so wenige Menschen sie nutzen.</blockquote>
      <h2>Praktische Einstiegspunkte</h2>
      <ul>
        <li><strong>Eine Ratssitzung besuchen</strong>: die meisten sind öffentlich und kostenlos</li>
        <li><strong>Ihren lokalen Stadtrat kontaktieren</strong>: schreiben Sie einen konkreten, prägnanten Brief oder eine E-Mail</li>
        <li><strong>An einem Konsultationsprozess teilnehmen</strong>: Kommunen führen Konsultationen durch — erscheinen Sie</li>
        <li><strong>Einer Gemeinschaftsvereinigung beitreten</strong>: Nachbarschaftsvereine sind die Basisinfrastruktur der Lokaldemokratie</li>
        <li><strong>Etwas starten</strong>: ein Gemeinschaftsgarten, eine Jugendveranstaltung</li>
      </ul>
      <h2>Langfristig aufbauen</h2>
      <p>Lokales demokratisches Engagement ist am wirksamsten, wenn es nachhaltig ist. Ein einzelnes Erscheinen bei einer Ratssitzung ändert nichts. Konsistente Präsenz, Beziehungsaufbau über Zeit und die Anhäufung von Glaubwürdigkeit und Wissen — das sind die Voraussetzungen für echten Einfluss.</p>
    """
    },
    '27': {
        'title_tr': 'Erasmus+ Gençlik Değişimi mi ESC mi: Hangi AB Programı Size Uygun?',
        'title_de': 'Erasmus+ Jugendaustausch vs. ESK: Welches EU-Programm passt zu dir?',
        'content_tr': """
      <p>AB tarafından finanse edilen mobiliteyi keşfeden bir genç veya gençlik örgütü iseniz, kısa süre içinde iki ana seçenekle karşılaşacaksınız: KA1 kapsamında Erasmus+ Gençlik Değişimleri ve Avrupa Dayanışma Birliği (ESC). Her ikisi de AB tarafından finanse edilmektedir. Her ikisi de sınırları aşan gençleri içermektedir. Ancak amaçları, yapıları ve uygunluk kriterleri anlamlı biçimde farklıdır — yanlış olanı seçmek zaman kaybına ve herkesin hayal kırıklığına yol açar.</p>
      <h2>Gençlik Değişimi Nedir?</h2>
      <p>Erasmus+ KA1 kapsamındaki bir Gençlik Değişimi, en az iki farklı ülkeden 13-30 yaş arası genç gruplarını kısa süreli bir yaygın eğitim programı için — genellikle 5 ila 21 gün — bir araya getirir. Değişim, katılımcılar tarafından değil STK'lar veya gençlik örgütleri tarafından organize edilir. Paylaşılan bir tema, program tasarımı ve kolaylaştırılmış bir öğrenme süreci vardır.</p>
      <p>Gençlik Değişimleri eğitim faaliyetleridir. Katılımcılar hizmet sunan gönüllüler değil — yapılandırılmış bir programla meşgul olan öğrenicilerdir.</p>
      <h2>Avrupa Dayanışma Birliği Nedir?</h2>
      <p>ESC, farklı bir felsefesiyle ayrışan bağımsız bir programdır. Ağırlıklı olarak gönüllülük, staj veya istihdam yoluyla topluluklara katkıda bulunmak isteyen 18-30 yaş arası gençler için tasarlanmıştır. Amiral gemisi faaliyeti bireysel gönüllülüktür: bir genç, başka bir ülkedeki bir ev sahibi örgüte 2 haftadan 12 aya kadar katılır ve belirli bir projeye veya hizmete katkıda bulunur.</p>
      <blockquote>Temel fark yöndedir. Gençlik Değişimi'nde program katılımcılara gelir. ESC'de katılımcı programa gider — ve nasıl işlediğinin bir parçası olur.</blockquote>
      <h2>Temel Farklılıklar</h2>
      <ul>
        <li><strong>Yaş</strong>: Gençlik Değişimleri 13-30 arası; ESC yalnızca 18-30</li>
        <li><strong>Süre</strong>: Gençlik Değişimleri genellikle 6-21 gün; ESC gönüllülüğü 2 haftadan 12 aya kadar</li>
        <li><strong>Grup mu bireysel mi</strong>: Gençlik Değişimleri grupları kapsar; ESC genellikle bireysel yerleştirmedir</li>
        <li><strong>Rol</strong>: Gençlik Değişimi katılımcıları öğrenicilerdir; ESC gönüllüleri ev sahibinin çalışmasına katkıda bulunanlar</li>
        <li><strong>Başvuran</strong>: Gençlik Değişimlerinde gönderen örgüt başvurur; ESC'de hem ev sahibi hem de gönderen örgütler kayıt olur ve gençler bireysel olarak başvurur</li>
      </ul>
      <h2>Durumunuz İçin Hangisi Doğru?</h2>
      <p>Uluslararası ortaklarla paylaşılan bir tema üzerine eğitim programı tasarlamak ve sunmak isteyen bir gençlik örgütüyseniz, Gençlik Değişimi doğru araçtır. Yurt dışındaki bir örgüte katkıda bulunarak uzun bir süre geçirmek isteyen bir gençseniz — dil öğrenmek, mesleki beceriler geliştirmek — ESC gönüllülüğü daha uygundur.</p>
    """,
        'content_de': """
      <p>Wenn Sie ein junger Mensch oder eine Jugendorganisation sind, die EU-finanzierte Mobilität erkundet, werden Sie schnell auf zwei Hauptoptionen stoßen: Erasmus+ Jugendaustausche unter KA1 und das Europäische Solidaritätskorps (ESK). Beide werden von der EU finanziert. Beide involvieren junge Menschen, die Grenzen überschreiten. Aber ihre Zwecke, Strukturen und Zulassungskriterien sind bedeutsam unterschiedlich.</p>
      <h2>Was ist ein Jugendaustausch?</h2>
      <p>Ein Jugendaustausch unter Erasmus+ KA1 bringt Gruppen junger Menschen im Alter von 13 bis 30 aus mindestens zwei verschiedenen Ländern für ein kurzfristiges non-formales Bildungsprogramm zusammen — typischerweise 5 bis 21 Tage. Jugendaustausche sind Bildungsaktivitäten. Die Teilnehmer sind keine Freiwilligen, die einen Dienst leisten — sie sind Lernende.</p>
      <h2>Was ist das Europäische Solidaritätskorps?</h2>
      <p>Das ESK ist ein eigenständiges Programm mit einer anderen Philosophie. Es ist primär für junge Menschen im Alter von 18 bis 30 konzipiert, die durch Freiwilligendienst, Praktikum oder Beschäftigung zu Gemeinschaften beitragen möchten.</p>
      <blockquote>Der grundlegende Unterschied ist die Richtung. Beim Jugendaustausch kommt das Programm zu den Teilnehmern. Beim ESK geht der Teilnehmer zum Programm — und wird Teil seines Funktionierens.</blockquote>
      <h2>Wichtigste Unterschiede</h2>
      <ul>
        <li><strong>Alter</strong>: Jugendaustausche akzeptieren 13–30; ESK ist nur 18–30</li>
        <li><strong>Dauer</strong>: Jugendaustausche sind typischerweise 6–21 Tage; ESK-Freiwilligendienst kann 2 Wochen bis 12 Monate dauern</li>
        <li><strong>Gruppe vs. Individuum</strong>: Jugendaustausche beinhalten Gruppen; ESK ist typischerweise individuelle Platzierung</li>
        <li><strong>Rolle</strong>: Jugendaustauschteilnehmer sind Lernende; ESK-Freiwillige sind Beitragende</li>
        <li><strong>Wer sich bewirbt</strong>: Beim Jugendaustausch bewirbt sich die Sendeorganisation; beim ESK registrieren sich sowohl Gast- als auch Sendeorganisationen</li>
      </ul>
      <h2>Welches ist für Ihre Situation richtig?</h2>
      <p>Wenn Sie eine Jugendorganisation sind, die ein Bildungsprogramm zu einem gemeinsamen Thema mit internationalen Partnern gestalten und durchführen möchten, ist ein Jugendaustausch das richtige Vehikel. Wenn Sie ein junger Mensch sind, der eine längere Zeit mit dem Beitrag zu einer Organisation im Ausland verbringen möchte, ist ESK-Freiwilligendienst angemessener.</p>
    """
    },
    '28': {
        'title_tr': 'Ulusal Ajanslar Erasmus+ Gençlik Başvurularını Nasıl Değerlendirir',
        'title_de': 'Wie Nationale Agenturen Erasmus+ Jugendanträge bewerten',
        'content_tr': """
      <p>Erasmus+ başvuruları, her ülkede AB gençlik finansmanını yönetmekten sorumlu kuruluşlar olan Ulusal Ajanslar tarafından değerlendirilir. Değerlendirme süreçlerini anlamak, ilk kez veya tekrar başvuran kişiler için en yüksek kaldıraçlı şeylerden biridir. Yine de çoğu rehber, değerlendiricilerin yazdıklarınızı nasıl okuduğundan çok ne yazacağınıza odaklanır.</p>
      <h2>Değerlendiriciler Kimdir?</h2>
      <p>Değerlendiriciler genellikle Ulusal Ajans tarafından görevlendirilen dış uzmanlar — gençlik çalışması ve yaygın eğitim alanında deneyimli uygulayıcılar, eğitmenler veya araştırmacılardır. Standartlaştırılmış bir değerlendirme ızgarasından çalışır ve başvurunun her bölümünü yayımlanmış kriterlere göre puanlarlar.</p>
      <p>Değerlendiriciler görece kısa sürede çok sayıda başvuru okur. Bu nedenle netlik, özgüllük ve mantıksal yapı yalnızca stilistik tercihler değil — pratik zorunluluklardır.</p>
      <h2>Değerlendirme Kriterleri</h2>
      <p>Gençlik Değişimi KA1 başvuruları için ana değerlendirme kriterleri ve yaklaşık ağırlıkları:</p>
      <ul>
        <li><strong>Alaka (% 30)</strong>: Proje gerçek bir ihtiyacı karşılıyor mu? Hedef grup iyi tanımlanmış mı? Avrupa/uluslararası boyut gerekçeli mi?</li>
        <li><strong>Proje tasarımının kalitesi (% 40)</strong>: Hedefler AKILLI (SMART) mı? Metodoloji hedeflere uyuyor mu? Program mantıklı ve iyi yapılandırılmış mı?</li>
        <li><strong>Proje ekibinin kalitesi (% 20)</strong>: Konsorsiyumun kapasitesi ve tamamlayıcılığı var mı? Roller net mi?</li>
        <li><strong>Etki (% 10)</strong>: Projenin ötesindeki sonuçların yayılması ve kullanımı için güvenilir bir plan var mı?</li>
      </ul>
      <blockquote>% 40 proje tasarım ağırlığı, çoğu başvurunun kazanıldığı veya kaybedildiği yerdir. İkna edici bir ihtiyaç analizi, program tasarımı mantıksal olarak ondan çıkmıyorsa hiçbir şey ifade etmez.</blockquote>
      <h2>Değerlendiricilerin Aradıkları</h2>
      <p>Alaka bölümünde değerlendiriciler, zaten yapmak istediğiniz bir faaliyeti gerekçelendirmek için bir ihtiyacı sonradan uydurmak yerine gerçek bir sorunu teşhis ettiğinize dair kanıt arar. Gerçek verilere atıfta bulunmak — anket sonuçları, gençlik politikası belgeleri, önceki program değerlendirmeleri — genel ifadelerden çok daha etkilidir.</p>
      <h2>Yaygın Ret Nedenleri</h2>
      <ul>
        <li>Belirli veri veya bağlam içermeyen belirsiz ihtiyaç analizi</li>
        <li>Ölçülemeyen öğrenme hedefleri ("katılımcılar hakkında daha fazla farkındalık kazanacak...")</li>
        <li>Pedagojik gerekçe açıklamadan faaliyetleri tanımlayan program tasarımı</li>
        <li>Hazırlık faaliyetleri veya Youthpass planı bulunmaması</li>
        <li>"Sosyal medyada paylaşacağız" ile sınırlı yayılım planı</li>
      </ul>
    """,
        'content_de': """
      <p>Erasmus+-Anträge werden von Nationalen Agenturen bewertet — den Einrichtungen in jedem Land, die für die Verwaltung von EU-Jugendfördermitteln verantwortlich sind. Zu verstehen, wie sie Anträge bewerten, ist eine der wertvollsten Sachen, die ein Erstantragsteller tun kann. Dennoch konzentrieren sich die meisten Leitfäden darauf, was zu schreiben ist, anstatt darauf, wie Bewerter lesen, was Sie geschrieben haben.</p>
      <h2>Wer sind die Bewerter?</h2>
      <p>Bewerter sind typischerweise externe Gutachter — Praktiker, Trainer oder Forscher mit Erfahrung in Jugendarbeit und non-formaler Bildung —, die von der Nationalen Agentur beauftragt wurden. Sie arbeiten mit einem standardisierten Bewertungsraster und bewerten jeden Abschnitt des Antrags anhand veröffentlichter Kriterien.</p>
      <h2>Die Bewertungskriterien</h2>
      <ul>
        <li><strong>Relevanz (30%)</strong>: Spricht das Projekt einen echten Bedarf an?</li>
        <li><strong>Qualität des Projektdesigns (40%)</strong>: Sind die Ziele SMART? Passt die Methodik zu den Zielen?</li>
        <li><strong>Qualität des Projektteams (20%)</strong>: Hat das Konsortium die Kapazität zur Durchführung?</li>
        <li><strong>Wirkung (10%)</strong>: Gibt es einen glaubwürdigen Verbreitungsplan?</li>
      </ul>
      <blockquote>Die 40%-Gewichtung für Qualität des Designs ist der Ort, wo die meisten Anträge gewonnen oder verloren werden. Eine überzeugende Bedarfsanalyse bedeutet nichts, wenn das Programmdesign nicht logisch daraus folgt.</blockquote>
      <h2>Häufige Ablehnungsgründe</h2>
      <ul>
        <li>Vage Bedarfsanalyse ohne spezifische Daten</li>
        <li>Lernziele, die nicht gemessen werden können</li>
        <li>Programmdesign, das Aktivitäten beschreibt ohne die pädagogische Begründung zu erklären</li>
        <li>Keine Vorbereitungsaktivitäten oder Youthpass-Plan beschrieben</li>
        <li>Verbreitungsplan beschränkt auf „wir werden in sozialen Medien teilen"</li>
      </ul>
    """
    },
    '29': {
        'title_tr': 'İlk Erasmus+ Projenizi Oluşturmak: Adım Adım Zaman Çizelgesi',
        'title_de': 'Ihr erstes Erasmus+-Projekt aufbauen: Eine Schritt-für-Schritt-Zeitlinie',
        'content_tr': """
      <p>İlk Erasmus+ projenizi yürütmek, çoğu kişinin beklediğinden önemli ölçüde daha fazla zaman alır. "Bir değişim yapmak istiyoruz" noktasından "katılımcılar uçakta" noktasına giden süreç genellikle 12-18 aydır. Bu zaman çizelgesini önceden anlamak — ve kritik karar noktalarının nerede olduğunu bilmek — yeni bir örgütün yapabileceği en değerli şeylerden biridir.</p>
      <h2>1. Aşama: Hazırlık ve Ortaklık (Aylar 1-4)</h2>
      <p>Başvurunun tek bir satırını yazmadan önce ortaklara ihtiyacınız var. Ve ortaklara yaklaşmadan önce ne yapmak istediğiniz ve neden hakkında net bir fikre ihtiyacınız var. Bu, yeni örgütlerin en sık acele ettiği ve projenin kalitesini en çok belirleyen aşamadır.</p>
      <p>Projenizin tematik odağını ve toplumunuzda hangi ihtiyacı karşıladığını tanımlayarak başlayın. Ardından çalışmaları sizinkini tamamlayan diğer ülkelerdeki örgütleri belirleyin. Bu, bir veritabanında bulduğunuz örgütlere soğuk e-postalar yoluyla değil, ilişkiler aracılığıyla gerçekleşmelidir.</p>
      <h2>2. Aşama: Başvuru Yazma (Aylar 4-6)</h2>
      <p>Çoğu Ulusal Ajansın yılda iki başvuru son tarihi vardır — genellikle Şubat ve Ekim'de, projeler 3-6 ay sonra başlar. Başvuru yazmaya ve geliştirmeye 4-6 hafta ayırın. Bu bir haftasonu yazdığınız bir belge değildir.</p>
      <blockquote>Başvuru bir sözleşmedir. İçindeki her taahhüt — metodoloji, değerlendirme, katılımcı profili, yayılım hakkında — sunmayı taahhüt ettiğinizdir. Yalnızca gerçekten yapabileceklerinizi yazın.</blockquote>
      <h2>3. Aşama: Karar ve Hazırlık (Aylar 6-10)</h2>
      <p>Ulusal Ajanslar genellikle başvuru son tarihinden 4-6 ay sonra kararlarını bildirir. Başarılı olunursa finansman koşullarını belirten bir hibe sözleşmesi alırsınız. Dikkatle okuyun.</p>
      <h2>4. Aşama: Değişim (Genellikle 6-10 Gün)</h2>
      <p>Değişimin kendisi projenin en görünür kısmıdır ancak — hazırlık kapsamlıysa — genellikle yönetilmesi en karmaşık kısım değildir.</p>
      <h2>5. Aşama: Takip ve Raporlama (Aylar 10-18)</h2>
      <p>Proje katılımcılar eve gittiğinde bitmez. Proje bitiş tarihinden itibaren 60 gün içinde sunulması gereken nihai rapor, faaliyetlerin, katılımcıların, harcamaların ve sonuçların dikkatli bir şekilde belgelenmesini gerektirir. Kayıtları süreç boyunca tutun — sonunda yeniden oluşturmaya çalışmayın.</p>
    """,
        'content_de': """
      <p>Ihr erstes Erasmus+-Projekt zu leiten ist deutlich zeitaufwändiger als die meisten Menschen erwarten. Der Zeitrahmen von „wir wollen einen Austausch machen" bis „Teilnehmer sitzen im Flugzeug" beträgt typischerweise 12–18 Monate. Diesen Zeitrahmen im Voraus zu verstehen ist eine der wertvollsten Dinge, die eine neue Organisation tun kann.</p>
      <h2>Phase 1: Vorbereitung und Partnerschaft (Monate 1–4)</h2>
      <p>Bevor Sie eine einzige Zeile eines Antrags schreiben, brauchen Sie Partner. Und bevor Sie Partner ansprechen, brauchen Sie ein klares Bild davon, was Sie tun wollen und warum. Dies ist die Phase, die neue Organisationen am häufigsten überstürzen.</p>
      <h2>Phase 2: Antragschreiben (Monate 4–6)</h2>
      <p>Die meisten Nationalen Agenturen haben zwei Antragsstichtage pro Jahr — typischerweise im Februar und Oktober. Planen Sie 4–6 Wochen für das Schreiben und Überarbeiten des Antrags ein.</p>
      <blockquote>Der Antrag ist ein Vertrag. Jede Verpflichtung, die Sie darin eingehen — über Methodik, Evaluation, Teilnehmerprofil, Verbreitung —, verpflichten Sie sich zu liefern. Schreiben Sie nur, was Sie tatsächlich tun können.</blockquote>
      <h2>Phase 3: Entscheidung und Vorbereitung (Monate 6–10)</h2>
      <p>Nationale Agenturen teilen typischerweise Entscheidungen innerhalb von 4–6 Monaten nach dem Antragsstichtag mit. Bei Erfolg erhalten Sie einen Fördervertrag, der die Bedingungen Ihrer Förderung festlegt.</p>
      <h2>Phase 4: Der Austausch (typischerweise 6–10 Tage)</h2>
      <p>Der Austausch selbst ist der sichtbarste Teil des Projekts, aber oft nicht der komplexeste zu managen — wenn die Vorbereitung gründlich war.</p>
      <h2>Phase 5: Nachbereitung und Berichterstattung (Monate 10–18)</h2>
      <p>Das Projekt endet nicht, wenn Teilnehmer nach Hause gehen. Der Abschlussbericht, der innerhalb von 60 Tagen nach dem Projektende bei der Nationalen Agentur einzureichen ist, erfordert sorgfältige Dokumentation. Führen Sie Aufzeichnungen während des gesamten Prozesses.</p>
    """
    },
    '30': {
        'title_tr': 'Gençlik Çalışmasında Etki Ölçümü: Yaptığınız İşin İşe Yaradığını Kanıtlamak',
        'title_de': 'Wirkungsmessung in der Jugendarbeit: Beweisen, dass das, was Sie tun, funktioniert',
        'content_tr': """
      <p>Gençlik çalışmasının bir etki sorunu var — etki eksikliğinden değil, bunu tarihsel olarak göstermekte kötü olmasından. Finansörler giderek artan biçimde kanıt talep ediyor. Politika yapıcılar veri istiyor. Ve gençler, neyin işe yarayıp neyin yaramadığı konusunda dürüst olan örgütleri hak ediyor. Temel etki ölçümünü gençlik projelerinize dahil etmek artık "olsa iyi olur" değil, profesyonel bir zorunluluktur.</p>
      <h2>Etki Ölçümü Nedir — Ve Ne Değildir</h2>
      <p>Etki ölçümü faaliyet raporlamasıyla aynı şey değildir. Ne yaptığınızı listelemek (altı atölye yürüttük, 42 katılımcı katıldı, bir araç seti ürettik) çıktı raporlamasıdır. Etki ölçümü farklı bir soru sorar: sonuç olarak ne değişti? Katılımcılar yeni yetkinlikler geliştirdi mi? Tutumlar değişti mi? Davranış değişti mi?</p>
      <h2>Değişim Teorisi: Başlangıç Noktanız</h2>
      <p>Etkiyi ölçebilmek için bir değişim teorisine ihtiyacınız var: faaliyetlerinizin sonucunda ne olacağına ve neden olacağına dair açık bir ifade. Değişim teoriniz olmadan veri toplarsınız ama ne anlama geldiğini bilemezsiniz.</p>
      <blockquote>Gençlik çalışması değerlendirmesindeki en yaygın hata, gerçekten önemli olanı değil, ölçmesi kolay olanı ölçmektir — katılım, memnuniyet puanları, faaliyet sayısı. Memnuniyet öğrenme değildir. Katılım meşguliyet değildir.</blockquote>
      <h2>İşe Yarayan Basit Araçlar</h2>
      <ul>
        <li><strong>Ön/son anketler</strong>: Faaliyetten önce ve sonra belirli yetkinlikleri veya tutumları ölçün</li>
        <li><strong>Yansıtıcı günlükler</strong>: Katılımcılardan faaliyet sırasında kısa günlük yansımalar yazmalarını isteyin</li>
        <li><strong>Takip görüşmeleri</strong>: Faaliyetten 3-6 ay sonra katılımcıların bir örneklemini arayın</li>
        <li><strong>En Önemli Değişim</strong>: Katılımcılardan kendi sözleriyle deneyimledikleri en önemli değişikliği tanımlamalarını isteyin</li>
      </ul>
      <h2>Dürüstçe Raporlama</h2>
      <p>Etki ölçümünün en zor kısmı bilmedikleriniz konusunda dürüst olmaktır. Finansörlere aşırı yükseltilmiş sonuçlar yerine sınırlı ama dürüst iddialar sunmak daha güvenilirdir.</p>
    """,
        'content_de': """
      <p>Jugendarbeit hat ein Wirkungsproblem — nicht weil es an Wirkung mangelt, sondern weil sie historisch schlecht darin war, es zu demonstrieren. Fördergeber fordern zunehmend Belege. Wirkungsmessung in Ihre Jugendprojekte einzubauen ist jetzt eine professionelle Notwendigkeit.</p>
      <h2>Was Wirkungsmessung ist — und was nicht</h2>
      <p>Wirkungsmessung ist nicht dasselbe wie Aktivitätsberichterstattung. Wirkungsmessung stellt eine andere Frage: Was hat sich verändert? Haben Teilnehmer neue Kompetenzen entwickelt? Haben sich Einstellungen verändert?</p>
      <h2>Wirkungstheorie: Ihr Ausgangspunkt</h2>
      <p>Bevor Sie Wirkung messen können, brauchen Sie eine Wirkungstheorie: eine klare Aussage darüber, was Sie glauben, was durch Ihre Aktivitäten passieren wird, und warum. Ohne eine Wirkungstheorie sammeln Sie Daten, ohne zu wissen, was sie bedeuten.</p>
      <blockquote>Der häufigste Fehler in der Bewertung von Jugendarbeit ist das Messen, was leicht zu messen ist — Anwesenheit, Zufriedenheitsbewertungen —, anstatt was wirklich wichtig ist. Zufriedenheit ist kein Lernen. Anwesenheit ist kein Engagement.</blockquote>
      <h2>Einfache Tools, die funktionieren</h2>
      <ul>
        <li><strong>Vor/nach-Befragungen</strong>: Messen Sie spezifische Kompetenzen oder Einstellungen vor und nach der Aktivität</li>
        <li><strong>Reflexionstagebücher</strong>: Bitten Sie Teilnehmer, kurze tägliche Reflexionen zu schreiben</li>
        <li><strong>Nachfolge-Interviews</strong>: Kontaktieren Sie eine Stichprobe von Teilnehmern 3–6 Monate nach der Aktivität</li>
        <li><strong>Bedeutsamste Veränderung</strong>: Bitten Sie Teilnehmer, die bedeutsamste Veränderung in eigenen Worten zu beschreiben</li>
      </ul>
      <h2>Ehrlich berichten</h2>
      <p>Der schwierigste Teil der Wirkungsmessung ist ehrlich zu sein über das, was Sie nicht wissen. Ehrliche, begrenzte Aussagen sind glaubwürdiger als aufgeblähte.</p>
    """
    },
    '31': {
        'title_tr': 'Başlangıç Seviyesi Hibe Yazarlığı: İlk Avrupa Gençlik Finansmanı Başvurunuz',
        'title_de': 'Fördermittelschreiben für Anfänger: Ihr erster europäischer Jugendfördermittelantrag',
        'content_tr': """
      <p>Hibe yazarlığı öğrenilmiş bir beceridir. Kimse bunu nasıl yapacağını bilerek doğmaz — ve iyi olanlarda çoğunlukla başarılı başvuruları okuma, başarısız olanlar üzerine geri bildirim alma ve değerlendiricilerin ne aradığını anlama sürecinin kombinasyonu yoluyla iyi olunur. Bu rehber bu yolculuğun başındaki kişiler içindir.</p>
      <h2>Önce Finansörün Mantığını Anlayın</h2>
      <p>Her hibe programı var olur çünkü biri — bir hükümet, bir vakıf, bir AB kurumu — belirli türde bir faaliyetin finanse edilmeye değer olduğuna karar vermiştir. Tek bir satır yazmadan önce finansörün neyi başarmaya çalıştığını ve projenizin bu gündemi nasıl hizmet ettiğini anlamanız gerekir.</p>
      <h2>İhtiyaç Analizi: Spesifik Olun</h2>
      <p>İlk kez başvuranlardaki en yaygın zayıflık belirsiz bir ihtiyaç analizidir. "Bölgemizdeki gençler istihdam ve sosyal katılım konusunda zorluklarla karşılaşıyor" bir ihtiyaç analizi değildir. İyi bir ihtiyaç analizi, projenizin ele aldığı spesifik boşluğu adlandırır, bunun kanıtını sunar ve neden bu projenin uygun yanıt olduğunu açıklar.</p>
      <blockquote>Bir finansörün sınırlı kaynakları vardır. Pek çok rakip ihtiyaçtan hangisini önceliklendireceğine karar vermeye çalışıyor. "Bu spesifik boşluğu belirledik, kanıtı budur ve önerilen yanıtımızın neden iyi eşleştiğini açıklayan örgüt" genel ifadelerle sorunları tanımlayana kıyasla çok daha ikna edicidir.</blockquote>
      <h2>Hedefler: AKILLI Olun Ya Da İşe Yaramaz</h2>
      <p>Başvurgunuzdaki her hedef Spesifik, Ölçülebilir, Ulaşılabilir, İlgili ve Zaman Bağlı olmalıdır. Her hedefi test edin: Proje sonunda birileri başvuruyu size verse, her hedefi gerçekleştirip gerçekleştirmediğinizi belirleyebilir miydi? Hayırsa, yeniden yazın.</p>
      <h2>Bütçe: Yaygın Hatalar</h2>
      <ul>
        <li>Program kılavuzunda sağlanan birim maliyet tablolarını kullanmamak</li>
        <li>Seyahat maliyetlerini düşük tahmin etmek</li>
        <li>Koordinasyon ve raporlama için personel zamanı gibi dolaylı maliyetleri unutmak</li>
        <li>Hangi maliyetlerin uygun olduğunu kontrol etmemek</li>
      </ul>
      <h2>Bir Belge Olarak Başvuru</h2>
      <p>Net yazın. Kısa paragraflar kullanın. Jargondan kaçının. Kısaltmaları ilk kullanımda açıklayın. Tutarlı olun. Yüksek sesle okuyun — bir cümleyi söylemek zorse okumak da zordur.</p>
    """,
        'content_de': """
      <p>Fördermittelschreiben ist eine erlernbare Fähigkeit. Niemand wird mit dem Wissen geboren, wie man es macht. Dieser Leitfaden richtet sich an Menschen am Anfang dieser Reise.</p>
      <h2>Verstehen Sie zuerst die Logik des Fördergebers</h2>
      <p>Jedes Förderprogramm existiert, weil jemand entschieden hat, dass eine bestimmte Art von Aktivität förderungswürdig ist. Bevor Sie eine Zeile schreiben, müssen Sie verstehen, was der Fördergeber zu erreichen versucht.</p>
      <h2>Die Bedarfsanalyse: Seien Sie spezifisch</h2>
      <p>Die häufigste Schwäche in Erstanträgen ist eine vage Bedarfsanalyse. Eine gute Bedarfsanalyse nennt die spezifische Lücke, die Ihr Projekt anspricht, belegt sie mit Beweisen und erklärt, warum dieses Projekt die angemessene Antwort ist.</p>
      <blockquote>Ein Fördergeber hat begrenzte Ressourcen. Die Organisation, die sagen kann „wir haben diese spezifische Lücke identifiziert, hier sind die Belege", ist viel überzeugender als eine, die Probleme in allgemeinen Begriffen beschreibt.</blockquote>
      <h2>Ziele: SMART oder nutzlos</h2>
      <p>Jedes Ziel in Ihrem Antrag muss Spezifisch, Messbar, Erreichbar, Relevant und Zeitgebunden sein. Testen Sie jedes Ziel: Könnte jemand, dem der Antrag am Ende des Projekts übergeben wird, bestimmen, ob Sie jedes Ziel erreicht haben?</p>
      <h2>Budget: Häufige Fehler</h2>
      <ul>
        <li>Nicht die im Programmhandbuch bereitgestellten Einheitskostentabellen verwenden</li>
        <li>Reisekosten unterschätzen</li>
        <li>Indirekte Kosten vergessen</li>
        <li>Nicht prüfen, welche Kosten förderfähig sind</li>
      </ul>
    """
    },
    '32': {
        'title_tr': 'Gençlik Örgütleri İçin Proje Yönetimi: İşe Yarayan Araçlar ve Yöntemler',
        'title_de': 'Projektmanagement für Jugendorganisationen: Tools und Methoden, die funktionieren',
        'content_tr': """
      <p>Çoğu gençlik örgütü yıllarca projeleri gayri resmi olarak yönetir — ve bu işe yarar, ta ki aniden işe yaramamaya başlayana kadar. Kaçırılan bir son tarih, karışık bir ortak, bir mali tutarsızlık, kritik proje bilgisiyle birlikte ayrılan bir ekip üyesi — bunlar gayri resmi yönetimin sonunda yarattığı krizlerdir. Temel proje yönetimi yapıları oluşturmak bürokratik olmak değildir. Bu, vaat ettiğiniz işi yapacak kadar güvenilir olmak demektir.</p>
      <h2>Temel: Her Gençlik Projesinin İhtiyaç Duyduğu Şeyler</h2>
      <p>Her proje, büyüklüğü ne olursa olsun, üç şeyden yararlanır: açık bir plan, iletişim yapısı ve kayıt tutma sistemi. En büyük tek proje yönetimi başarısızlığı küçük STK'larda kritik bilgilerin — kişiler, şifreler, mali kayıtlar, ortak sözleşmeleri — yalnızca bir kişinin kafasında veya e-posta hesabında depolanmasıdır.</p>
      <h2>Küçük Ekipler İçin Araçlar</h2>
      <ul>
        <li><strong>Notion veya Trello</strong>: görev takibi, paylaşılan belgeler ve proje planlaması için</li>
        <li><strong>Google Workspace</strong>: işbirlikçi belge düzenleme ve paylaşılan sürücüler için</li>
        <li><strong>Airtable</strong>: katılımcıları, ortakları ve bütçe kalemlerini veritabanı formatında takip etmek için</li>
        <li><strong>Slack veya Signal grupları</strong>: ekip iletişimi için</li>
      </ul>
      <blockquote>En iyi proje yönetim aracı ekibinizin gerçekten kullandığı araçtır. Ekibin yarısının görmezden geldiği karmaşık bir sistem, herkesin koruduğu basit bir paylaşılan belgeden daha kötüdür.</blockquote>
      <h2>Mali Yönetim: Vazgeçilmezler</h2>
      <p>AB tarafından finanse edilen projeler için mali yönetim opsiyonel değildir. Proje için ayrı bir banka hesabına, her işlemi fiş ile kaydeden bir gider takip sistemine ihtiyacınız var. Her fişi saklayın. Kağıt fişleri anında fotoğraflayın. Aylık hesap mutabakatı yapın.</p>
      <h2>Ortakları Yönetmek</h2>
      <p>Uluslararası projeler yurtiçi projelerden daha kasıtlı ortak yönetimi gerektirir. Baştan iletişim normları üzerinde anlaşın. Kararları yazılı olarak belgeleyin. Yanlış anlamaları erken ele alın — kendi kendilerine çözülmezler.</p>
    """,
        'content_de': """
      <p>Die meisten Jugendorganisationen managen Projekte jahrelang informell — und es funktioniert, bis es plötzlich nicht mehr funktioniert. Grundlegende Projektmanagementstrukturen aufzubauen bedeutet nicht, bürokratisch zu werden. Es bedeutet, zuverlässig genug zu sein, die Arbeit zu tun, die man versprochen hat.</p>
      <h2>Die Grundlagen: Was jedes Jugendprojekt braucht</h2>
      <p>Jedes Projekt, unabhängig von der Größe, profitiert von drei Dingen: einem klaren Plan, einer Kommunikationsstruktur und einem Aufzeichnungssystem. Der größte einzelne Projektmanagementfehler in kleinen NGOs ist, kritische Informationen nur im Kopf oder E-Mail-Konto einer Person zu speichern.</p>
      <h2>Tools für kleine Teams</h2>
      <ul>
        <li><strong>Notion oder Trello</strong>: für Aufgabenverfolgung und geteilte Dokumentation</li>
        <li><strong>Google Workspace</strong>: für kollaborative Dokumentbearbeitung</li>
        <li><strong>Airtable</strong>: für die Verfolgung von Teilnehmern, Partnern und Budgetposten</li>
        <li><strong>Slack oder Signal-Gruppen</strong>: für Teamkommunikation</li>
      </ul>
      <blockquote>Das beste Projektmanagement-Tool ist dasjenige, das Ihr Team tatsächlich verwendet. Ein ausgefeiltes System, das die Hälfte des Teams ignoriert, ist schlechter als ein einfaches geteiltes Dokument, das alle pflegen.</blockquote>
      <h2>Finanzmanagement: Das Unverzichtbare</h2>
      <p>Für EU-geförderte Projekte ist Finanzmanagement nicht optional. Sie brauchen ein separates Bankkonto für das Projekt. Bewahren Sie jeden Beleg auf. Gleichen Sie Ihre Konten monatlich ab.</p>
      <h2>Partner managen</h2>
      <p>Internationale Projekte erfordern bewussteres Partnermanagement als inländische. Vereinbaren Sie Kommunikationsnormen von Anfang an. Dokumentieren Sie Entscheidungen schriftlich. Gehen Sie Missverständnisse frühzeitig an.</p>
    """
    },
    '33': {
        'title_tr': 'Gönüllüleri Elde Tutmak: İnsanları Gerçekten Meşgul Tutan Stratejiler',
        'title_de': 'Freiwillige halten: Strategien, die Menschen wirklich engagiert halten',
        'content_tr': """
      <p>Küçük bir STK'daki ortalama gönüllü süresi 18 aydan azdır. Çoğu örgüt bunu gönüllü çalışmanın kaçınılmaz bir özelliği olarak görür. Gönüllüleri 3, 5 veya 10 yıl boyunca elinde tutan örgütler bunu bir yönetim zorluğu olarak görür — ve gerçekten bunu ele alan uygulamalar geliştirmiştir.</p>
      <h2>Gönüllüler Neden Ayrılır?</h2>
      <p>Çıkış görüşmeleri ve gönüllü bağlılık araştırmaları tutarlı biçimde aynı ayrılış nedenlerini tespit eder: katkılarının değer görmediğini hissetmek, ne yapmaları gerektiğine dair belirsiz beklentiler, örgütten zayıf iletişim ve rolde öğrenmediklerini veya büyümediklerini hissetmek. "Yeterli zaman yok" — gönüllülerin kamuoyuna en sık verdiği neden — neredeyse hiçbir zaman dürüst çıkış verilerinde görünmez. Genellikle yukarıdakilerin nazik bir ifadesidir.</p>
      <blockquote>Gönüllüler meşgul oldukları için ayrılmaz. Maliyet-fayda analizi değiştiği için ayrılırlar. Sizin işiniz o dengeyi pozitif tutmaktır.</blockquote>
      <h2>İlk Katılım Aşaması Kritiktir</h2>
      <p>Gönüllü elde tutma araştırmaları tutarlı biçimde şunu gösterir: en yüksek ayrılma riski ilk 90 gündedir. Bu dönemi geçiren gönüllüler önemli ölçüde daha uzun süre kalma eğilimindedir. Yine de çoğu STK gönüllüye kısa bir karşılama yaptıktan sonra kendi yolunu bulmaya bırakır.</p>
      <h2>Gönüllülerin Gerçekten İstedikleri</h2>
      <ul>
        <li><strong>Anlamlı iş</strong>: örgütün misyonuyla bağlantılı görevler</li>
        <li><strong>Net beklentiler</strong>: ne yapmaları gerektiğini, ne zamana kadar ve hangi standartta bilmek</li>
        <li><strong>Tanınma</strong>: katkılarının görüldüğünün ve değerlendirildiğinin düzenli kabulü</li>
        <li><strong>Öğrenme ve gelişim</strong>: beceriler geliştirme fırsatları</li>
        <li><strong>Topluluk</strong>: bir ekibe ait olma hissi</li>
      </ul>
      <h2>Gönüllü Kültürü Oluşturmak</h2>
      <p>Gönüllüleri en iyi elinde tutan örgütler, ücretli personelin gönüllülere ödenmemiş işçiler olarak değil meslektaşlar olarak davrandığı örgütlerdir. YouthTICK olarak tamamen gönüllülerden oluşan bir örgütüz. Bu makaledeki her şey bize de diğerleri kadar uygulanır.</p>
    """,
        'content_de': """
      <p>Die durchschnittliche Freiwilligenlaufzeit bei einer kleinen NGO beträgt weniger als 18 Monate. Die Organisationen, die Freiwillige für 3, 5 oder 10 Jahre halten, behandeln dies als Managementherausforderung — und haben Praktiken entwickelt, die sie wirklich angehen.</p>
      <h2>Warum Freiwillige gehen</h2>
      <p>Konsistent werden dieselben Abgangsgründe identifiziert: das Gefühl, dass ihr Beitrag nicht geschätzt wird, unklare Erwartungen, schlechte Kommunikation und das Gefühl, nicht zu lernen oder zu wachsen.</p>
      <blockquote>Freiwillige gehen nicht, weil sie beschäftigt sind. Sie gehen, weil sich die Kosten-Nutzen-Analyse verschiebt. Ihre Aufgabe ist es, diese Balance positiv zu halten.</blockquote>
      <h2>Die Onboarding-Phase ist entscheidend</h2>
      <p>Das höchste Abgangsrisiko liegt in den ersten 90 Tagen. Freiwillige, die diese Phase überstehen und sich wirklich in der Organisation verankert fühlen, bleiben deutlich länger.</p>
      <h2>Was Freiwillige wirklich wollen</h2>
      <ul>
        <li><strong>Bedeutungsvolle Arbeit</strong>: Aufgaben, die mit der Mission der Organisation verbunden sind</li>
        <li><strong>Klare Erwartungen</strong>: wissen, was sie tun sollen, bis wann und in welchem Standard</li>
        <li><strong>Anerkennung</strong>: regelmäßige Bestätigung, dass ihr Beitrag gesehen und geschätzt wird</li>
        <li><strong>Lernen und Entwicklung</strong>: Möglichkeiten zur Kompetenzentwicklung</li>
        <li><strong>Gemeinschaft</strong>: das Gefühl, zu einem Team zu gehören</li>
      </ul>
      <h2>Eine Freiwilligenkultur aufbauen</h2>
      <p>Die Organisationen, die Freiwillige am besten halten, sind diejenigen, bei denen bezahlte Mitarbeiter Freiwillige als Kollegen behandeln, nicht als unbezahlte Arbeitskräfte. Bei YouthTICK sind wir eine vollständig ehrenamtlich geführte Organisation. Alles in diesem Artikel trifft auf uns genauso zu.</p>
    """
    },
    '34': {
        'title_tr': 'Gençler İçin Yeşil Beceriler: Neler ve Neden Önemli',
        'title_de': 'Grüne Kompetenzen für junge Menschen: Was sie sind und warum sie wichtig sind',
        'content_tr': """
      <p>2022'de başlatılan Avrupa Komisyonu'nun Yeşil Beceriler Gündemi, Avrupa işgücü genelinde yeşil becerilerin geliştirilmesini önümüzdeki on yılın en acil iş piyasası önceliklerinden biri olarak belirledi. Gençlik örgütleri için yeşil becerilerin gerçekte ne olduğunu — ve gençlerin bunları geliştirmesine nasıl yardımcı olunacağını — anlamak, mevcut politika ortamında ilgili olmanın temel bir parçası haline geliyor.</p>
      <h2>Yeşil Beceriler Nedir?</h2>
      <p>AB yeşil becerileri "sürdürülebilir ve kaynak verimli bir toplumda yaşamak, onu geliştirmek ve desteklemek için gereken bilgi, yetenek, değerler ve tutumlar" olarak tanımlar. Yeşil beceriler son derece teknik olanlara kadar uzanır (yenilenebilir enerji sistemleri mühendisliği) ve genel olarak uygulanabilir olanlara (sistem düşüncesi, sürdürülebilirlik liderliği).</p>
      <blockquote>Yeşil beceriler çevreye bağlılar için bir uzmanlık değil. Neredeyse her sektördeki profesyoneller için temel yetkinlikler haline geliyor. Bunları geliştirmeyen gençler giderek artan bir dezavantajla karşı karşıyadır.</blockquote>
      <h2>Gençlik Örgütlerinin Geliştirebileceği Yeşil Beceriler</h2>
      <ul>
        <li><strong>Sistem düşüncesi</strong>: çevresel, sosyal ve ekonomik sistemlerin nasıl etkileştiğini anlamak</li>
        <li><strong>Sürdürülebilirlik iletişimi</strong>: karmaşık çevre bilgisini farklı kitlelere aktarma</li>
        <li><strong>Yeşil proje yönetimi</strong>: çevresel etkiye açık dikkatle faaliyetler planlama</li>
        <li><strong>Sivil çevre katılımı</strong>: çevre politikasının nasıl yapıldığını anlamak</li>
        <li><strong>Ekolojik okuryazarlık</strong>: ekosistemlerin nasıl işlediğinin temel anlayışı</li>
      </ul>
      <h2>Gençlik Programlarında Yeşil Becerileri Entegre Etmek</h2>
      <p>Yeşil becerileri geliştirmek her gençlik programını çevre atölyesine dönüştürmek anlamına gelmez. En etkili yaklaşım, yeşil beceri gelişimini mevcut faaliyetlere gömmektir: çevre temalarını içeren Erasmus+ değişimleri tasarlamak, neden azaltıldığını tartışarak karbon ayak izini azaltan proje faaliyetleri yürütmek.</p>
    """,
        'content_de': """
      <p>Die Grüne Kompetenzagenda der Europäischen Kommission aus dem Jahr 2022 identifizierte die Entwicklung grüner Kompetenzen in der europäischen Belegschaft als eine der dringlichsten Arbeitsmarktprioritäten des kommenden Jahrzehnts.</p>
      <h2>Was sind grüne Kompetenzen?</h2>
      <p>Die EU definiert grüne Kompetenzen als „das Wissen, die Fähigkeiten, die Werte und die Einstellungen, die benötigt werden, um in einer nachhaltigen und ressourceneffizienten Gesellschaft zu leben, sie zu entwickeln und zu unterstützen."</p>
      <blockquote>Grüne Kompetenzen sind keine Spezialisierung für umweltbewusste Menschen. Sie werden zu Basiskompetenzen für Fachleute in fast jedem Sektor. Junge Menschen, die sie nicht entwickeln, haben einen wachsenden Nachteil.</blockquote>
      <h2>Grüne Kompetenzen, die Jugendorganisationen entwickeln können</h2>
      <ul>
        <li><strong>Systemdenken</strong>: Verstehen, wie Umwelt-, Sozial- und Wirtschaftssysteme interagieren</li>
        <li><strong>Nachhaltigkeitskommunikation</strong>: komplexe Umweltinformationen für verschiedene Zielgruppen übersetzen</li>
        <li><strong>Grünes Projektmanagement</strong>: Aktivitäten mit expliziter Aufmerksamkeit für Umweltauswirkungen planen</li>
        <li><strong>Ökologische Kompetenz</strong>: grundlegendes Verständnis davon, wie Ökosysteme funktionieren</li>
      </ul>
      <h2>Grüne Kompetenzen in Jugendprogramme integrieren</h2>
      <p>Grüne Kompetenzen zu entwickeln bedeutet nicht, jedes Jugendprogramm in einen Umwelt-Workshop zu verwandeln. Der effektivste Ansatz ist, die Entwicklung grüner Kompetenzen in bestehende Aktivitäten einzubetten.</p>
    """
    },
    '35': {
        'title_tr': 'Topluluğunuzda Gençlik Öncülüğünde Çevre Projesi Nasıl Başlatılır',
        'title_de': 'Wie man ein jugendbewegtes Umweltprojekt in seiner Gemeinde startet',
        'content_tr': """
      <p>Gençlik öncülüğünde bir çevre projesi başlatmak için resmi bir örgüte, AB finansmanına veya uzman kimlik bilgilerine ihtiyacınız yoktur. Avrupa'daki en etkili yerel çevre girişimlerinin bazıları, kendi mahallelerinde görebildikleri gerçek bir sorunla ve bir somut adım atmaya istekli üç ya da dört gençle başladı. İşte bu adımı — ve ardından gelen adımları — nasıl atacağınız.</p>
      <h2>Gerçek Bir Yerel Sorunla Başlayın</h2>
      <p>Gençlik öncülüğündeki çevre projelerindeki en yaygın hata, spesifik bir sorun yerine bir hevesle başlamaktır — "topluluğumuzda iklim değişikliğini ele almak istiyoruz." İklim değişikliği gerçek ve acildir, ancak bir tasarım sorunu değildir. Kirletilmiş bir kentsel dere, yetersiz yeşil alan, tek kullanımlık plastik tüketimi — bunlar tasarım sorunlarıdır.</p>
      <blockquote>İyi çalışan küçük bir grubun enerjisi, herhangi bir topluluk projesinin sahip olduğu en güçlü kaynaktır. Onu koruyun: normlar üzerinde erkenden anlaşın, çatışmaları doğrudan ele alın.</blockquote>
      <h2>Küçük Başlayın, Sonra Büyeyin</h2>
      <p>Herhangi bir şeyi test etmeden önce büyük, karmaşık bir girişim planlamak cazibesine direntin. Önce küçük bir pilot yürütün — tek bir temizlik etkinliği, tek günlük bir atölye, bir mahalle anketi. Neyin işe yaradığını, kimlerin geldiğini, hangi engellerin var olduğunu ve hangi kaynaklara ihtiyacınız olduğunu öğrenmek için kullanın.</p>
      <h2>Mevcut Ağlara Bağlanın</h2>
      <p>Sıfırdan başlamanıza gerek yok. Gençlik iklim ağları, çevre STK'ları, belediye sürdürülebilirlik birimleri ve üniversite araştırma merkezleri potansiyel ortak ve bağlantı noktalarıdır.</p>
      <h2>Projenizi Finanse Etmek</h2>
      <p>Erken aşamalı, yerel odaklı gençlik çevre projeleri için en erişilebilir finansman kaynakları: belediye gençlik fonları, topluluk vakfı küçük hibeleri, yerel işletmelerden kurumsal sosyal sorumluluk programları ve kitlesel fonlama. Erasmus+ bir uluslararası boyut eklemek istediğinizde geçerli olur.</p>
    """,
        'content_de': """
      <p>Sie brauchen keine formelle Organisation, keine EU-Förderung oder Expertenkenntnisse, um ein jugendbewegtes Umweltprojekt zu starten. Einige der effektivsten lokalen Umweltinitiativen in Europa begannen mit drei oder vier jungen Menschen, einem echten Problem, das sie in ihrer eigenen Nachbarschaft sehen konnten, und der Bereitschaft, einen konkreten Schritt zu machen.</p>
      <h2>Mit einem echten lokalen Problem beginnen</h2>
      <p>Der häufigste Fehler in jugendbewegten Umweltprojekten ist der Beginn mit einem Ehrgeiz — „wir wollen den Klimawandel in unserer Gemeinde ansprechen" — anstatt mit einem spezifischen Problem. Verbringen Sie Zeit damit, mit Menschen in Ihrer Gemeinde über das zu sprechen, was sie wirklich bemerken und was ihnen wichtig ist.</p>
      <blockquote>Die Energie einer gut funktionierenden kleinen Gruppe ist die stärkste Ressource, die ein Gemeinschaftsprojekt haben kann. Schützen Sie sie: vereinbaren Sie früh Normen, gehen Sie Konflikte direkt an.</blockquote>
      <h2>Klein anfangen, dann wachsen</h2>
      <p>Widerstehen Sie der Versuchung, eine große, komplexe Initiative zu planen, bevor Sie irgendetwas getestet haben. Führen Sie zuerst ein kleines Pilotprojekt durch — eine einzige Säuberungsaktion, ein eintägiger Workshop. Nutzen Sie es, um zu lernen, was funktioniert.</p>
      <h2>Mit bestehenden Netzwerken verbinden</h2>
      <p>Sie müssen nicht von null anfangen. Jugendklimanetzwerke, Umwelt-NGOs, kommunale Nachhaltigkeitsabteilungen sind alle potenzielle Partner, Berater und Verbinder.</p>
      <h2>Ihr Projekt finanzieren</h2>
      <p>Für frühphasige, lokal ausgerichtete Jugendumweltprojekte sind die zugänglichsten Finanzierungsquellen: kommunale Jugendfonds, kleine Gemeinschaftsstiftungszuschüsse, CSR-Programme lokaler Unternehmen und Crowdfunding.</p>
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
