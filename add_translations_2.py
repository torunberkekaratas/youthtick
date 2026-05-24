#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os

TRANS = {
'11': {
'title_tr': "Gençlik Çalışanları İçin Tasarım Düşüncesi: 5 Adımlı Pratik Rehber",
'title_de': "Design Thinking für Jugendfachkräfte: Ein praktischer 5-Schritte-Leitfaden",
'content_tr': """
      <p>Tasarım düşüncesi işletme okullarında, inovasyon laboratuvarlarında ve kurumsal eğitim programlarında en yaygın öğretilen çerçevelerden biri haline geldi. Gençlik çalışması benimsemekte daha yavaş kaldı — bu talihsiz, çünkü tasarım düşüncesi süreci neredeyse mükemmel biçimde iyi gençlik çalışmasının zaten nasıl işlediğiyle örtüşüyor.</p>
      <h2>Tasarım Düşüncesi Nedir (ve Değildir)</h2>
      <p>Tasarım düşüncesi, tasarladığınız kişileri derinlemesine anlamayı, olası çözümlerin hızlı prototiplerini oluşturmayı ve yinelemeli test ile iyileştirmeyi öncelikli kılan bir problem çözme yaklaşımıdır. Uzmanların cevaplara sahip olduğunu varsaymaz. Cevapların dinleme, yaratma ve başarısızlıktan öğrenme süreciyle ortaya çıktığını varsayar.</p>
      <h2>Beş Aşama</h2>
      <h3>1. Empati Kur</h3>
      <p>Herhangi bir şey tasarlamadan önce, tasarladığınız kişileri anlamanız gerekir. Gençlik çalışmasında bu, gençlere gerçekte neye ihtiyaç duyduklarını sormak — ne ihtiyaç duyduklarını varsaydığınızı değil — ve yanıtları ciddiye almak anlamına gelir.</p>
      <h3>2. Tanımla</h3>
      <p>Araştırmanızdan, çözmeye çalıştığınız temel problemi belirleyin. "Kasabamızdaki gençler sivil yaşamdan kopuk" bir tasarım problemi değildir. "Kasabamızdaki gençler görüşlerinin duyulduğunu ama ardından karar alıcılar tarafından görmezden gelindiğini hissediyor, bu da katılıma karşı sinizm yaratıyor" bir tasarım problemidir.</p>
      <h3>3. Fikir Üret</h3>
      <p>Hiçbirini değerlendirmeden önce çok sayıda olası çözüm üretin. İnovasyonun en büyük düşmanı erken yakınsama — ilk iyi kulağa gelen fikre yerleşmektir.</p>
      <h3>4. Prototip Oluştur</h3>
      <p>En iyi fikirlerinizin kaba, hızlı versiyonlarını oluşturun. Prototip bitmiş bir ürün değil — fiziksel hale getirilmiş bir sorudur. Amaç bir şeyi mümkün olan en hızlı ve ucuz biçimde test edilebilir hale getirmektir.</p>
      <blockquote>İlk prototipi insanlara göstermekten utanıyorsanız, çok uzun beklediniz. Amaç etkilemek değil öğrenmektir.</blockquote>
      <h3>5. Test Et</h3>
      <p>Prototipi gerçek kullanıcıların önüne koyun — gençlik çalışmasında gerçek gençlerin — ve ne olduğunu izleyin. Size nasıl kullandıklarını göstermelerini isteyin. Nerede zorlandıklarını, nerede başarılı olduklarını ve beklediğinizden farklı nasıl davrandıklarını fark edin.</p>
      <h2>Gençlik Çalışmasında Uygulamak</h2>
      <p>Tasarım düşüncesi yeni gençlik programları geliştirmek, mevcut programları yeniden tasarlamak veya gençlerle birlikte toplum problemlerini ele almak için özellikle iyi çalışır.</p>
""",
'content_de': """
      <p>Design Thinking ist zu einem der am weitesten verbreiteten Rahmen in Business Schools, Innovationslaboren und Unternehmensschulungsprogrammen geworden. Die Jugendarbeit war langsamer damit — was bedauerlich ist, denn der Design-Thinking-Prozess passt nahezu perfekt zur Funktionsweise guter Jugendarbeit.</p>
      <h2>Was Design Thinking ist (und nicht ist)</h2>
      <p>Design Thinking ist ein Problemlösungsansatz, der tiefes Verständnis der Menschen, für die man gestaltet, schnelles Prototyping möglicher Lösungen sowie iteratives Testen und Verfeinern priorisiert. Es geht nicht davon aus, dass Experten die Antworten haben — es geht davon aus, dass Antworten durch einen strukturierten Prozess des Zuhörens, Schaffens und Lernens aus Fehlern entstehen.</p>
      <h2>Die fünf Phasen</h2>
      <h3>1. Empathisieren</h3>
      <p>Bevor Sie irgendetwas gestalten, müssen Sie die Menschen verstehen, für die Sie gestalten. In der Jugendarbeit bedeutet das, junge Menschen zu fragen, was sie wirklich brauchen — nicht was Sie annehmen, dass sie brauchen — und die Antworten ernst zu nehmen.</p>
      <h3>2. Definieren</h3>
      <p>Identifizieren Sie aus Ihrer Forschung das Kernproblem, das Sie lösen möchten. „Junge Menschen in unserer Stadt sind vom bürgerlichen Leben losgelöst" ist kein Designproblem. „Junge Menschen in unserer Stadt haben das Gefühl, dass ihre Meinungen gehört, dann aber von Entscheidungsträgern ignoriert werden" ist eines.</p>
      <h3>3. Ideenfindung</h3>
      <p>Generieren Sie eine große Anzahl möglicher Lösungen, bevor Sie eine davon bewerten. Der größte Feind der Innovation ist vorzeitige Konvergenz — sich auf die erste gut klingende Idee zu einigen.</p>
      <h3>4. Prototyping</h3>
      <p>Bauen Sie grobe, schnelle Versionen Ihrer besten Ideen. Ein Prototyp ist kein fertiges Produkt — er ist eine physisch gemachte Frage. Das Ziel ist, etwas so schnell und günstig wie möglich testbar zu machen.</p>
      <blockquote>Wenn Sie sich für Ihren ersten Prototypen schämen, haben Sie zu lange gewartet, ihn Menschen zu zeigen. Der Punkt ist zu lernen, nicht zu beeindrucken.</blockquote>
      <h3>5. Testen</h3>
      <p>Stellen Sie den Prototypen echten Nutzerinnen und Nutzern vor — in der Jugendarbeit echten jungen Menschen — und beobachten Sie, was passiert. Bitten Sie sie zu zeigen, wie sie ihn nutzen, anstatt es zu erzählen.</p>
      <h2>Anwendung in der Jugendarbeit</h2>
      <p>Design Thinking funktioniert besonders gut für die Entwicklung neuer Jugendprogramme, die Neugestaltung bestehender oder die Bearbeitung von Gemeinschaftsproblemen mit jungen Menschen als Co-Designer.</p>
"""
},
'12': {
'title_tr': "Sosyal Girişim mi STK mı: Hangi Model Gençlik Girişiminize Uyar?",
'title_de': "Sozialunternehmen vs. NGO: Welches Modell passt zu Ihrer Jugendinitiative?",
'content_tr': """
      <p>Bir gençlik girişimi için fikriniz var. Belki gençlerin işlettiği bir toplum kafe, bir beceri eğitim programı, bir akran mentorluk ağı ya da gönüllüleri yerel kuruluşlarla buluşturan bir uygulama. Şimdi birçok kurucunun şaşırtıcı bulduğu yapısal soru geliyor: Bu bir STK mı, dernek mi, sosyal girişim mi, yoksa kooperatif mi olmalı?</p>
      <h2>Temel Ayrım</h2>
      <p>Sivil toplum kuruluşu ile sosyal girişim arasındaki temel fark değerlerle ilgili değil — gelir modeliyle ilgilidir. Bir STK esas olarak hibelere, bağışlara ve kamu fonlarına dayanır. Bir sosyal girişim gelirinin büyük bölümünü piyasada mal veya hizmet satışından elde eder.</p>
      <p>Her ikisi de sosyal misyon peşinde koşabilir. Her ikisi de derin değer odaklı olabilir. Soru şu: Modeliniz bir piyasa mı, yoksa hayırseverlik mi gerektiriyor?</p>
      <h2>STK Ne Zaman Mantıklı?</h2>
      <p>Çalışmanız esas olarak ödeme yapamayacak kişilere fayda sağladığında ve değerlerinizi paylaşan fon sağlayıcılara bu çalışma için savunuculuk yapabildiğinizde STK modelini seçin.</p>
      <blockquote>Sosyal girişim, yan tarafta iyi işler yapan bir işletme değildir. Sosyal misyonun modele gömülü olduğu bir işletmedir — işi yapmak ve iyi yapmak aynı eylemdir.</blockquote>
      <h2>Hibrit Yol</h2>
      <p>En başarılı gençlik kuruluşlarının çoğu hibrit yapıdadır. Gençlik çalışması ve Erasmus+ projelerini yürüten bir STK veya derneği var, yanı sıra kazanılmış gelir sağlayan ve hibe bağımlılığını azaltan sosyal girişim faaliyetleri var.</p>
      <h2>Gençlik Öncülüğündeki Girişimler İçin</h2>
      <p>Yeni başlayan gençler için dernek formu genellikle en erişilebilirdir — kurulması daha kolay, fon sağlayıcılar tarafından iyi anlaşılmış ve gelişmek için yeterince esnek. Yapı misyona hizmet etmeli, tersi değil.</p>
""",
'content_de': """
      <p>Sie haben eine Idee für eine Jugendinitiative. Vielleicht ein von jungen Menschen betriebenes Gemeinschaftscafé, ein Qualifizierungsprogramm, ein Peer-Mentoring-Netzwerk oder eine App, die Freiwillige mit lokalen Organisationen verbindet. Jetzt kommt die strukturelle Frage: Soll das eine NGO, ein Verein, ein Sozialunternehmen oder eine Genossenschaft sein?</p>
      <h2>Der Kernunterschied</h2>
      <p>Der grundlegende Unterschied zwischen einer Nichtregierungsorganisation und einem Sozialunternehmen geht nicht um Werte — er geht um das Erlösmodell. Eine NGO verlässt sich hauptsächlich auf Zuschüsse, Spenden und öffentliche Förderung. Ein Sozialunternehmen erwirtschaftet den Großteil oder den gesamten Umsatz durch Handel: den Verkauf von Waren oder Dienstleistungen auf dem Markt.</p>
      <blockquote>Ein Sozialunternehmen ist kein Unternehmen, das nebenbei Gutes tut. Es ist ein Unternehmen, in dem die soziale Mission im Modell eingebettet ist — wo die Sache zu tun und Gutes zu tun dieselbe Handlung sind.</blockquote>
      <h2>Der hybride Weg</h2>
      <p>Viele der erfolgreichsten Jugendorganisationen sind Hybride. Sie haben eine NGO oder einen Verein als Kern — für Jugendarbeit, Erasmus+-Projekte und Gemeinschaftsprogramme — neben Sozialunternehmen-Aktivitäten, die Einnahmen generieren und die Abhängigkeit von Zuschüssen reduzieren.</p>
      <h2>Für jugendgeführte Initiativen</h2>
      <p>Für junge Menschen am Anfang ist die Vereinsform oft am zugänglichsten — einfacher zu gründen, von Fördergebern gut verstanden und flexibel genug, um sich weiterzuentwickeln. Die Struktur sollte der Mission dienen, nicht umgekehrt.</p>
"""
},
'13': {
'title_tr': "Yerel Fikirden Avrupa Ölçeğine: Gençlik Öncülüğündeki Kuruluşlardan Dersler",
'title_de': "Von der lokalen Idee zur europäischen Skalierung: Lektionen jugendgeführter Organisationen",
'content_tr': """
      <p>Avrupa'nın en başarılı gençlik kuruluşlarının çoğu üç kişinin, paylaşılan bir sorunun ve hiç paranın olmadığı bir odada başladı. Sınır ötesinde faaliyet gösterecek, AB fonları çekecek ve politikayı etkileyecek büyüklüğe erişenler, bunu işletme okulu oyun kitabını izleyerek yapmadı.</p>
      <h2>Programdan Değil, Sorundan Başlayın</h2>
      <p>Ölçeklenen kuruluşlar, gerçek bir sorunun keskin bir tanısıyla başlayanlardır — soruya eklemek istedikleri bir program fikriyle değil. Kuruluşunuz çözmeye çalıştığı bir sorunla tanımlanırsa — endüstri sonrası topluluklarda gençlik işsizliği, kırsal gençlerin Avrupa ağlarından yalıtılmışlığı, demokratik katılım açığı — faaliyetlerinizi neyin işe yaradığını öğrendikçe geliştirebilirsiniz.</p>
      <h2>İhtiyaç Duymadan Önce Ağı İnşa Edin</h2>
      <p>Avrupa'da başarıyla ölçeklenen her gençlik kuruluşu bunu ilişkiler aracılığıyla yaptı. Bu ilişkiler neredeyse hiçbir zaman işlemsel olarak kurulmadı. Yıllar içinde gerçek işbirliğinden büyüdü.</p>
      <blockquote>İlk Erasmus+ KA2 projeniz için başvuru, ortaklarınızla yaptığınız ilk konuşma olmamalıdır. Zaten içinde güven bulunan bir ilişkinin resmileştirilmesi olmalıdır.</blockquote>
      <h2>Kurumsal Kapasite Seçenek Değildir</h2>
      <p>Birçok gençlik öncülüğündeki kuruluş — finansal sistemler, İK süreçleri, yönetişim yapıları — bunları bürokrasiyle ve taban ruhunu yitirmekle özdeşleştirdikleri için örgütsel altyapı kurmaya direnir. Bu bir hatadır.</p>
      <h2>Küçük Kalmayı Ne Zaman Bilin</h2>
      <p>Her başarılı gençlik kuruluşu Avrupa ölçeğinde faaliyet göstermeye çalışmamalıdır. Gençlik gelişimindeki en iyi çalışmanın bir kısmı, topluluğunu derinden tanıyan ve eşleşen ilişkilere sahip küçük, köklü yerel kuruluşlar tarafından yapılmaktadır. Ölçek, derinlikten özünde daha iyi değildir.</p>
""",
'content_de': """
      <p>Die meisten erfolgreichen europäischen Jugendorganisationen begannen in einem Raum mit drei Menschen, einem gemeinsamen Problem und kein Geld. Diejenigen, die grenzüberschreitend operierten, EU-Förderung anzogen und Politik beeinflussten, taten dies nicht nach dem Business-School-Playbook.</p>
      <h2>Mit dem Problem beginnen, nicht mit dem Programm</h2>
      <p>Die Organisationen, die skalieren, sind diejenigen, die mit einer scharfen Diagnose eines echten Problems begannen — nicht mit einer Programmidee, an die sie dann ein Problem zu knüpfen versuchten. Wenn Ihre Organisation durch ein Problem definiert wird, das sie zu lösen versucht, können Sie Ihre Aktivitäten weiterentwickeln, wenn Sie mehr darüber lernen, was funktioniert.</p>
      <blockquote>Der Antrag für Ihr erstes Erasmus+ KA2-Projekt sollte nicht das erste Gespräch sein, das Sie mit Ihren Partnern führen. Es sollte die Formalisierung einer Beziehung sein, in der bereits Vertrauen vorhanden ist.</blockquote>
      <h2>Institutionelle Kapazität ist keine Option</h2>
      <p>Viele jugendgeführte Organisationen widersetzen sich dem Aufbau organisatorischer Infrastruktur — Finanzsysteme, HR-Prozesse, Governance-Strukturen — weil sie diese mit Bürokratie und dem Verlust des Basisgeistes assoziieren. Das ist ein Fehler.</p>
      <h2>Wissen, wann man klein bleibt</h2>
      <p>Nicht jede erfolgreiche Jugendorganisation sollte versuchen, auf europäischer Ebene zu operieren. Einige der besten Arbeit in der Jugendentwicklung wird von kleinen, tief verwurzelten lokalen Organisationen geleistet. Größe ist nicht grundsätzlich besser als Tiefe.</p>
"""
},
'14': {
'title_tr': "Avrupa Yeşil Mutabakatı: Gençlik Kuruluşları İçin Ne Anlama Geliyor",
'title_de': "Der Europäische Green Deal: Was er für Jugendorganisationen bedeutet",
'content_tr': """
      <p>Avrupa Yeşil Mutabakatı — AB'nin 2050'ye kadar iklim tarafsızlığına ulaşmak için amiral gemisi politika çerçevesi — esas olarak bir gençlik politikası değil. Ancak gençlik kuruluşları, gençlik çalışma pratiği ve kuruluşların çalıştığı gençler için çıkarımları önemlidir.</p>
      <h2>Yeşil Mutabakat Gerçekte Nedir</h2>
      <p>Avrupa Yeşil Mutabakatı, AB'yi "adil ve müreffeh, modern, kaynak verimli ve rekabetçi bir ekonomiye sahip bir topluma" dönüştürmeyi amaçlayan bir politika, yasal düzenleme ve finansman mekanizmaları paketidir. Başlık hedefi: 2050'ye kadar net sıfır sera gazı emisyonu, 2030'a kadar %55 azalma.</p>
      <h2>Gençlik Kuruluşları İçin Ne Anlama Geliyor</h2>
      <p>Önce finansman var. Yeşil Mutabakat, birden fazla program genelinde önemli kaynakların kilidini açıyor — yalnızca LIFE+ veya Horizon Avrupa gibi belirgin olanları değil, aynı zamanda Erasmus+'ı (sürdürülebilirlik kesişen öncelik olarak), Avrupa Sosyal Fonu+'nı ve Avrupa Bölgesel Kalkınma Fonu'nu da.</p>
      <blockquote>Yeşil Mutabakat, gençlik çalışması için bir kısıtlama değildir. Bir davettir. Sürdürülebilir bir ekonomiye geçiş, tam olarak iyi gençlik çalışmasının geliştirdiği yetkinlikleri gerektirir: uyum sağlama, sivil katılım, sistemik düşünme ve farklılıklar üzerinden çalışabilme.</blockquote>
      <h2>Adil Geçiş: Sosyal Boyut</h2>
      <p>Dezavantajlı topluluklarla çalışan gençlik kuruluşları için Yeşil Mutabakat'taki en önemli kavram "adil geçiş"tir — yeşil ekonomiye geçişin bazı toplulukları ve işçileri diğerlerinden daha sert etkileyeceğinin ve bunun açıkça ele alınması gerektiğinin kabulüdür.</p>
      <h2>Sürdürülebilirliği Kendi Pratiğinize Gömmek</h2>
      <p>Erasmus+ artık başvuru sahiplerinden hareketlilik faaliyetlerinin çevresel etkisini göz önünde bulundurmalarını açıkça istiyor. Bu, yalnızca fon nedenleri için değil, kurumsal bütünlük meselesi olarak da ciddiye alınmaya değer.</p>
""",
'content_de': """
      <p>Der Europäische Green Deal — das EU-Vorzeige-Politikrahmenwerk zur Erreichung der Klimaneutralität bis 2050 — ist in erster Linie keine Jugendpolitik. Aber seine Auswirkungen auf Jugendorganisationen, die Jugendarbeitspraxis und die jungen Menschen, mit denen Organisationen arbeiten, sind erheblich.</p>
      <h2>Was der Green Deal eigentlich ist</h2>
      <p>Der Europäische Green Deal ist ein Paket aus Politiken, Gesetzgebungsakten und Finanzierungsmechanismen, das darauf abzielt, die EU in „eine faire und prosperierende Gesellschaft mit einer modernen, ressourceneffizienten und wettbewerbsfähigen Wirtschaft" zu verwandeln.</p>
      <h2>Was es für Jugendorganisationen bedeutet</h2>
      <p>Erstens gibt es Finanzierung. Der Green Deal erschließt erhebliche Ressourcen über mehrere Programme — nicht nur die offensichtlichen wie LIFE+ oder Horizon Europe, sondern auch Erasmus+ (mit Nachhaltigkeit als Querschnittspriorität), den Europäischen Sozialfonds+ und den Europäischen Fonds für regionale Entwicklung.</p>
      <blockquote>Der Green Deal ist keine Einschränkung für die Jugendarbeit. Er ist eine Einladung. Der Übergang zu einer nachhaltigen Wirtschaft erfordert genau die Kompetenzen, die gute Jugendarbeit entwickelt: Anpassungsfähigkeit, bürgerschaftliches Engagement, Systemdenken und die Fähigkeit, über Unterschiede hinweg zu arbeiten.</blockquote>
      <h2>Gerechter Übergang: Die soziale Dimension</h2>
      <p>Das wichtigste Konzept im Green Deal für Jugendorganisationen, die mit benachteiligten Gemeinschaften arbeiten, ist „gerechter Übergang" — die Anerkennung, dass die Umstellung auf eine grüne Wirtschaft einige Gemeinschaften und Arbeitnehmer härter treffen wird als andere.</p>
      <h2>Nachhaltigkeit in die eigene Praxis einbetten</h2>
      <p>Erasmus+ verlangt von Antragstellern nun explizit, die Umweltauswirkungen ihrer Mobilitätsaktivitäten zu berücksichtigen. Das ist es wert, nicht nur aus Fördergründen ernst zu nehmen, sondern als Frage der organisatorischen Integrität.</p>
"""
},
'15': {
'title_tr': "Gençlerde İklim Kaygısı: Çevre Korkusunu Eyleme Dönüştürmek",
'title_de': "Klimaangst bei jungen Menschen: Öko-Angst in Handlung umwandeln",
'content_tr': """
      <p>2021'de The Lancet'te yayımlanan önemli bir çalışma, on ülkede 16-25 yaş arasında 10.000 genç insanı inceledi. Yarısından fazlası — %56'sı — "insanlığın mahkûm olduğuna" inandığını söyledi. Yaklaşık dörtte üçü geleceğin "korkunç" olduğunu söyledi. Bu niş bir bulgu değil. İklim kaygısı, 2020'lerde büyümenin belirleyici psikolojik gerçekliklerinden biri haline geldi.</p>
      <h2>İklim Kaygısı Nedir</h2>
      <p>İklim kaygısı — bazen eko-kaygı olarak da adlandırılır — bir akıl hastalığı değildir. Gerçek bir tehdide verilen rasyonel bir yanıttır. Araştırmacılar bunu "çevresel yıkıma yönelik kronik korku" olarak tanımlar — gezegenin durumu ve geleceği hakkında kalıcı, çoğu zaman bunaltıcı bir sıkıntı hissi.</p>
      <h2>Çaresizlik Riski</h2>
      <p>İklim kaygısı, katılım yerine felce yol açtığında bir sorun haline gelir. Krizin ölçeği eylemin anlamsız göründüğü kadar bunaltıcı hissettirdiğinde.</p>
      <blockquote>Çaresizlik ahlaki bir başarısızlık değildir. Gerçekten korkunç olan bir duruma verilen normal bir yanıttır. Soru, gençlere onu aşmaları için araçlar verip vermediğimizdir — faillik, bağlantı ve eyleme doğru.</blockquote>
      <h2>Gençlik Çalışanları Ne Yapabilir</h2>
      <p>Neyin yardımcı olduğuna dair araştırma açıktır: faillik ve topluluk. Harekete geçme kapasitesine sahip olduklarını hisseden — küçük yollarla bile — ve endişelerini ve değerlerini paylaşan başkalarıyla bağlantılı olan gençler, izole ve çaresiz hissedenlerden çok daha az iklim kaygısı gösteriyor.</p>
      <ul>
        <li><strong>Duygulara alan yaratın</strong>: iklim kaygısının üzerinden hızla problem çözmeye geçmeyin</li>
        <li><strong>Yerel ve anlık eyleme odaklanın</strong>: toplum bahçeleri, yerel savunuculuk, okul sürdürülebilirlik projeleri</li>
        <li><strong>Yerleli küresele bağlayın</strong>: yerel eylemin daha büyük hareketlerle nasıl bağlantılı olduğunu gösterin</li>
        <li><strong>İşe yarayanları kutlayın</strong>: yenilenebilir enerji geçişi, genişleyen koruma alanları, büyüyen gençlik siyasi temsili</li>
      </ul>
      <h2>Kaygıdan Savunuculuğa</h2>
      <p>Amaç iklim kaygısını ortadan kaldırmak değil — belirli düzeyde bir endişe uygun ve motive edicidir. Amaç gençlerin o kaygıyla sürdürülebilir bir ilişki geliştirmelerine yardımcı olmaktır.</p>
""",
'content_de': """
      <p>Im Jahr 2021 untersuchte eine wegweisende Studie im Lancet 10.000 junge Menschen im Alter von 16–25 Jahren in zehn Ländern. Mehr als die Hälfte — 56% — gab an zu glauben, dass „die Menschheit dem Untergang geweiht ist". Fast drei Viertel sagten, die Zukunft sei „erschreckend". Das ist kein Nischenbefund. Klimaangst ist zu einer der bestimmenden psychologischen Realitäten des Aufwachsens in den 2020ern geworden.</p>
      <h2>Was Klimaangst ist</h2>
      <p>Klimaangst — manchmal auch Öko-Angst genannt — ist keine psychische Erkrankung. Sie ist eine rationale Reaktion auf eine reale Bedrohung. Forscher definieren sie als „chronische Angst vor dem Untergang der Umwelt".</p>
      <h2>Das Risiko der Verzweiflung</h2>
      <p>Klimaangst wird zum Problem, wenn sie zu Lähmung statt zu Engagement führt. Wenn das Ausmaß der Krise so überwältigend erscheint, dass Handeln sinnlos wirkt.</p>
      <blockquote>Verzweiflung ist kein moralisches Versagen. Es ist eine normale Reaktion auf eine Situation, die wirklich beängstigend ist. Die Frage ist, ob wir jungen Menschen die Werkzeuge geben, um sie zu durchleben — in Richtung Handlungsfähigkeit, Verbindung, Aktion.</blockquote>
      <h2>Was Jugendfachkräfte tun können</h2>
      <p>Die Forschung darüber, was hilft, ist klar: Handlungsfähigkeit und Gemeinschaft. Junge Menschen, die das Gefühl haben, handeln zu können — sogar in kleinen Dingen — und in Gemeinschaften eingebettet sind, die ihre Sorgen und Werte teilen, zeigen deutlich weniger Klimaangst.</p>
      <ul>
        <li><strong>Raum für Gefühle schaffen</strong>: nicht vorschnell über Klimaangst zum Problemlösen übergehen</li>
        <li><strong>Auf lokale und unmittelbare Maßnahmen fokussieren</strong>: Gemeinschaftsgärten, lokales Advocacy, Nachhaltigkeitsprojekte</li>
        <li><strong>Lokal mit Global verbinden</strong>: zeigen, wie lokale Maßnahmen mit größeren Bewegungen zusammenhängen</li>
        <li><strong>Erfolge feiern</strong>: die Energiewende, wachsende Schutzgebiete, wachsende politische Jugendvertretung</li>
      </ul>
"""
},
'16': {
'title_tr': "Gençlik Grupları İçin Sürdürülebilir Etkinlik Planlaması: Pratik Kontrol Listesi",
'title_de': "Nachhaltige Veranstaltungsplanung für Jugendgruppen: Eine praktische Checkliste",
'content_tr': """
      <p>Erasmus+ artık başvuru sahiplerinden projelerinin çevresel etkisini ele almalarını istiyor. Finansman gerekliliklerinin ötesinde, etik bir boyut da var: programlarınız sürdürülebilirlikle ilgiliyse, bu programları yürütme biçiminiz bunu yansıtmalıdır.</p>
      <h2>Seyahat: En Büyük Değişken</h2>
      <p>Çoğu gençlik değişimi ve eğitim etkinliği için seyahat, projenin karbon ayak izinin en büyük payını oluşturur. Yapabileceğiniz en etkili karar, uygulanabilir olduğu her yerde uçuş yerine tren seyahatini tercih etmektir.</p>
      <h2>Mekan Seçimi</h2>
      <ul>
        <li>Çevre sertifikalarına sahip mekanları tercih edin (Green Key, AB Çevre Etiketi)</li>
        <li>En yakın tren/otobüs istasyonundan toplu taşımayla erişilebilir mekanları seçin</li>
        <li>Mekanlara enerji kaynakları, gıda tedariki ve atık yönetimi uygulamaları hakkında soru sorun</li>
      </ul>
      <h2>Gıda ve İkram</h2>
      <p>Gıda tercihleri herhangi bir etkinlikte en önemli — ve en görünür — sürdürülebilirlik kararlarından biridir. Bitkisel ağırlıklı ikram, et ağırlıklı menülere kıyasla çok daha düşük emisyona sahiptir.</p>
      <blockquote>Kültürlerarası gece et şöleni olmak zorunda değil. Her kültürün kendi gıda kimliğinin merkezinde yer alan bitkisel tabanlı yemekleri var.</blockquote>
      <h2>Materyaller ve Baskı</h2>
      <ul>
        <li>Dijital program kitapçıklarına geçin ve materyalleri QR kod veya paylaşılan sürücü aracılığıyla paylaşın</li>
        <li>Tek kullanımlık markalı ürünlerden (kalem, defter, kordon) kaçının</li>
        <li>Fiziksel materyaller üretiyorsanız geri dönüştürülmüş kağıt ve soya bazlı mürekkepler kullanın</li>
      </ul>
      <h2>Ölçün ve Raporlayın</h2>
      <p>Projenizin emisyonlarını tahmin etmek için basit bir karbon ayak izi hesaplayıcısı kullanın. Sonuçları katılımcılarla paylaşın. Erasmus+ raporlamanızda kullanın. Yıldan yıla ilerlemenizi takip edin.</p>
""",
'content_de': """
      <p>Erasmus+ fordert Antragsteller nun auf, die Umweltauswirkungen ihrer Projekte anzugehen. Jenseits der Förderanforderungen gibt es eine ethische Dimension: Wenn Ihre Programminhalte über Nachhaltigkeit handeln, sollte die Art und Weise, wie Sie diese Programme durchführen, dies widerspiegeln.</p>
      <h2>Reisen: Die größte Variable</h2>
      <p>Bei den meisten Jugendbegegnungen und Trainingsveranstaltungen macht das Reisen den größten Anteil des CO₂-Fußabdrucks des Projekts aus. Die wirkungsvollste Entscheidung ist, wo immer möglich Bahnreisen gegenüber Flügen zu wählen.</p>
      <h2>Standortwahl</h2>
      <ul>
        <li>Standorte mit Umweltzertifizierungen bevorzugen (Green Key, EU Ecolabel)</li>
        <li>Mit öffentlichen Verkehrsmitteln erreichbare Standorte wählen</li>
        <li>Standorte nach Energiequellen, Lebensmittelbeschaffung und Abfallmanagement befragen</li>
      </ul>
      <h2>Essen und Catering</h2>
      <p>Pflanzliches Catering hat deutlich geringere Emissionen als fleischreiche Menüs. Lokale und saisonale Beschaffung reduziert Lebensmittelkilometer.</p>
      <blockquote>Die interkulturelle Nacht muss kein Fleischfest sein. Jede Kultur hat pflanzliche Gerichte, die zentral für ihre Lebensmittelidentität sind.</blockquote>
      <h2>Materialien und Druck</h2>
      <ul>
        <li>Auf digitale Programmhefte umsteigen und Materialien per QR-Code teilen</li>
        <li>Einweg-Markenartikel vermeiden</li>
        <li>Wenn physische Materialien nötig sind, Recyclingpapier und pflanzenbasierte Tinten verwenden</li>
      </ul>
      <h2>Messen und berichten</h2>
      <p>Verwenden Sie einen einfachen CO₂-Rechner, um die Emissionen Ihres Projekts abzuschätzen. Teilen Sie die Ergebnisse mit Teilnehmenden. Nutzen Sie sie in Ihrer Erasmus+-Berichterstattung.</p>
"""
},
'17': {
'title_tr': "Döngüsel Ekonomi ve Gençlik: Yarının Yeşil İşleri İçin Beceriler",
'title_de': "Kreislaufwirtschaft und Jugend: Fähigkeiten für die grünen Jobs von morgen",
'content_tr': """
      <p>Döngüsel ekonomi, Avrupa'nın yeşil dönüşümündeki merkezi kavramlardan biridir ve önümüzdeki on yılda emek piyasasının ödüllendireceği becerileri gerçek anlamda yeniden şekillendiriyor. Gençleri ekonomik geleceğe hazırlayan gençlik çalışanları için döngüsel ekonominin gerçekte ne anlama geldiğini anlamak artık seçimlik arka plan bilgisi değil; zorunludur.</p>
      <h2>Doğrusal ve Döngüsel: Temel Ayrım</h2>
      <p>Geleneksel endüstriyel ekonomi doğrusaldır: kaynakları çıkar, ürünleri üret, kullan, at. Döngüsel ekonomi, atık kavramını tamamen ortadan kaldırmayı hedefler: ürünler kapalı döngülerde yeniden kullanılacak, onarılacak, yenilenecek ve geri dönüştürülecek biçimde tasarlanır.</p>
      <blockquote>Şu anda Avrupa'da en çok talep gören yeşil beceri güneş paneli kurabilme yeteneği değil — sistemleri anlayabilme yeteneğidir: malzemelerin nasıl aktığını, değerin nerede yaratıldığını, nerede kaybolduğunu ve süreçlerin her ikisini de döngüde tutacak biçimde nasıl yeniden tasarlanacağını.</blockquote>
      <h2>Aktarılabilir Beceriler</h2>
      <p>Teknik becerilerin ötesinde, döngüsel ekonomi yaygın eğitimin özellikle iyi geliştirdiği bazı yetkinlikleri ödüllendiriyor. Sistemik düşünme — karmaşık bir sistemin parçalarının nasıl etkileştiğini görme yeteneği. Disiplinler arası sınırlarda işbirlikçi problem çözme. Yaratıcı yeniden kullanım ve tasarım düşüncesi.</p>
      <h2>Gençlik Kuruluşları Ne Yapabilir</h2>
      <ul>
        <li>İş gölgeleme ve staj için yerel döngüsel ekonomi işletmeleriyle ortaklık kurun</li>
        <li>Döngüsel ekonomi prensiplerini sürdürülebilirlik programlarına dahil edin</li>
        <li>Gençleri Avrupa Döngüsel Ekonomi Paydaş Platformu ile bağlantılandırın</li>
        <li>Tamir kafeleri, upcycling atölyeleri ve materyal yeniden kullanım projelerini öğrenme faaliyetleri olarak kullanın</li>
      </ul>
""",
'content_de': """
      <p>Die Kreislaufwirtschaft ist eines der zentralen Konzepte in Europas grünem Übergang — und eines, das wirklich neu gestaltet, welche Fähigkeiten der Arbeitsmarkt im kommenden Jahrzehnt belohnen wird. Für Jugendfachkräfte, die junge Menschen auf wirtschaftliche Zukünfte vorbereiten, ist das Verständnis der Kreislaufwirtschaft keine optionale Hintergrundkenntnis mehr. Es ist wesentlich.</p>
      <h2>Linear vs. zirkulär: Der Kernunterschied</h2>
      <p>Die traditionelle Industriewirtschaft ist linear: Ressourcen gewinnen, Produkte herstellen, nutzen, wegwerfen. Die Kreislaufwirtschaft zielt darauf ab, das Konzept von Abfall vollständig zu eliminieren: Produkte werden so gestaltet, dass sie in geschlossenen Kreisläufen wiederverwendet, repariert, aufgearbeitet und recycelt werden können.</p>
      <blockquote>Die am stärksten nachgefragte grüne Fähigkeit in Europa ist derzeit nicht die Fähigkeit, Solaranlagen zu installieren — es ist die Fähigkeit, Systeme zu verstehen: wie Materialien fließen, wo Wert entsteht, wo er verloren geht, und wie Prozesse neu gestaltet werden können, um beides im Kreislauf zu halten.</blockquote>
      <h2>Übertragbare Kompetenzen</h2>
      <p>Jenseits technischer Fähigkeiten belohnt die Kreislaufwirtschaft einige Kompetenzen, die die non-formale Bildung besonders gut entwickelt: Systemdenken, kollaboratives Problemlösen über Disziplingrenzen hinaus, kreatives Wiederverwenden und Design Thinking.</p>
      <h2>Was Jugendorganisationen tun können</h2>
      <ul>
        <li>Mit lokalen Kreislaufwirtschaftsunternehmen für Job-Shadowing und Praktika kooperieren</li>
        <li>Kreislaufwirtschaftsprinzipien in Nachhaltigkeitsprogramme integrieren</li>
        <li>Junge Menschen mit der Europäischen Kreislaufwirtschafts-Stakeholder-Plattform verbinden</li>
        <li>Reparier-Cafés, Upcycling-Workshops und Materialwiederverwendungsprojekte nutzen</li>
      </ul>
"""
},
'18': {
'title_tr': "Türk-Alman Gençlik Diyaloğu: Değişim Yoluyla Önyargıları Kırmak",
'title_de': "Türkisch-Deutsches Jugenddialog: Stereotypen durch Austausch überwinden",
'content_tr': """
      <p>Türkiye ile Almanya arasındaki ilişki, Avrupa tarihinin en karmaşık ve sonuçları en önemli ikili ilişkilerinden biridir. On yıllarca süren işçi göçü, iki ülke arasındaki derin aile bağları, ortak NATO üyeliği, tartışmalı AB üyeliği ve her iki tarafta da kalıcı kültürel yanlış anlaşılmalar tarafından şekillendirilmiş bu ilişki daha gerçek diyaloğa ihtiyaç duyuyor — daha azına değil.</p>
      <h2>Tarihsel Arka Plan</h2>
      <p>1960'ların misafir işçi (Gastarbeiter) anlaşmaları, Batı Almanya'ya yüz binlerce Türk işçi getirdi. Onların torunları — şimdi üç ya da dört nesil ileriye — Avrupa'daki en büyük Türk diaspora topluluğunu oluşturuyor: yaklaşık 3 milyon kişi. Ancak on yıllarca ortak coğrafyaya rağmen, Türk kökenli topluluklar ile çoğunluk Alman toplumu arasındaki ilişki çoğu zaman mesafe, yanlış anlama ve karşılıklı kalıp yargılarla karakterize edilmeye devam ediyor.</p>
      <blockquote>Türk bir gençle iki hafta boyunca ortak bir proje üzerinde işbirliği yapan, fikir tartışan, birlikte yemek yiyen ve kültürel yanlış anlamaları açıkça yöneten genç Alman, geldiği basit kalıp yargıları sürdürme olasılığı düşüktür.</blockquote>
      <h2>Bu Pratikte Ne Anlama Geliyor</h2>
      <p>İşe yarayan Türk-Alman değişimleri birkaç ortak özelliği paylaşır. İki ülke arasındaki tarihi doğrudan ele alırlar — zor konulardan kaçınmak değil, bunlar için kolaylaştırılmış alan yaratmak. Her iki ülkeden Türk miras mensubu katılımcıları dahil ederek daha karmaşık üçlü bir diyalog yaratırlar.</p>
      <h2>YouthTICK Boyutu</h2>
      <p>Türk-Alman gençlik diyaloğu YouthTICK'in misyonunun kalbindedir. Bu diyalog için gerçek alan yaratan programlar geliştiriyoruz — her şeyi çözmek için değil, iki ülke arasındaki ilişkiyi biraz daha insancıl kılacak türden gerçek bir karşılaşma yaratmak için.</p>
""",
'content_de': """
      <p>Die Beziehung zwischen der Türkei und Deutschland ist eine der komplexesten und folgenreichsten bilateralen Beziehungen in der europäischen Geschichte. Geprägt durch Jahrzehnte der Arbeitsmigration, tiefe Familienbande über zwei Länder hinweg, gemeinsame NATO-Mitgliedschaft, umstrittenen EU-Beitritt und anhaltende kulturelle Missverständnisse auf beiden Seiten — diese Beziehung braucht mehr echten Dialog, nicht weniger.</p>
      <h2>Der historische Hintergrund</h2>
      <p>Die Gastarbeiterabkommen der 1960er Jahre brachten Hunderttausende türkische Arbeitnehmer nach Westdeutschland. Ihre Nachkommen — jetzt drei oder vier Generationen später — bilden die größte türkische Diaspora-Gemeinschaft in Europa: etwa 3 Millionen Menschen.</p>
      <blockquote>Der junge Deutsche, der zwei Wochen lang mit türkischen Gleichaltrigen an einem gemeinsamen Projekt zusammengearbeitet hat — über Ideen gestritten, zusammen gekocht, kulturelle Missverständnisse offen navigiert hat — wird kaum dieselben simplen Stereotype aufrechterhalten, mit denen er ankam.</blockquote>
      <h2>Was das in der Praxis bedeutet</h2>
      <p>Türkisch-deutsche Austausche, die funktionieren, teilen mehrere Merkmale. Sie sprechen die Geschichte zwischen den beiden Ländern direkt an — nicht durch Vermeidung schwieriger Themen, sondern durch Schaffung facilitierter Räume dafür.</p>
      <h2>Die YouthTICK-Dimension</h2>
      <p>Der türkisch-deutsche Jugenddialog steht im Mittelpunkt von YouthTICKs Mission. Wir entwickeln Programme, die echten Raum für diesen Dialog schaffen — nicht um alles zu lösen, sondern um die Art realer Begegnung zu schaffen, die die Beziehung zwischen zwei Ländern ein wenig menschlicher macht.</p>
"""
},
'19': {
'title_tr': "Süper Güç Olarak Çok Dillilik: Gençlik Programlarında Dil Öğrenimi",
'title_de': "Mehrsprachigkeit als Superkraft: Sprachlernen in Jugendprogrammen",
'content_tr': """
      <p>Uluslararası gençlik değişiminin merkezinde bir paradoks var: özünde çok dilli bir faaliyet olan bu etkinlik, genellikle herkesin İngilizce konuştuğu varsayımıyla yürütülüyor. Çoğu Erasmus+ değişimi çalışma dili olarak İngilizce kullanır — bu, en zayıf İngilizcesiyle katılanların tüm etkinliği mücadele ederek geçireceği, en güçlü İngilizcesiyle katılanların ise tartışmalara hâkim olacağı anlamına gelir.</p>
      <h2>Dilin Göründüğünden Daha Fazla Önemi Var</h2>
      <p>Dil yalnızca bir iletişim aracı değildir. Düşüncenin bir yapısı, kültürün bir kabı ve gücün bir mekanizmasıdır. Tüm katılımcıları bazıları için anadil, diğerleri için yabancı dil olan bir dilde çalışmaya zorladığınızda, hiçbir kolaylaştırma becerisinin tam olarak telafi edemeyeceği sistematik bir dezavantaj yaratırsınız.</p>
      <blockquote>Paylaşılan bir dil olmadan katılımcıların iletişim kurmasını gerektiren bir etkinlik tasarladığınızda — jest, imge, hareket, ses kullanarak — kültürlerarası iletişimin gerçekte ne olduğunu keşfedersiniz: kelimelerin akıcı değişimi değil, anlam üzerine yaratıcı müzakere.</blockquote>
      <h2>Çok Dillilik ve İstihdam Edilebilirlik</h2>
      <p>Etik ve pedagojik boyutların ötesinde, çok dillilik giderek değerli bir emek piyasası varlığıdır. Birden fazla dilde anlamlı biçimde iletişim kurabilen gençler — yalnızca ders kitabı ifadelerini ezberlemekten değil, gerçek kültürlerarası etkileşimleri yönetebilmekten — her sektördeki işverenler tarafından aranmaktadır.</p>
""",
'content_de': """
      <p>Im Herzen des internationalen Jugendaustauschs liegt ein Paradoxon: Er ist eine inhärent mehrsprachige Aktivität, die oft so operiert, als würde jeder Englisch sprechen. Die meisten Erasmus+-Begegnungen verwenden Englisch als Arbeitssprache — was bedeutet, dass die Teilnehmenden mit den schwächsten Englischkenntnissen die gesamte Veranstaltung kämpfend verbringen, während diejenigen mit den stärksten Englischkenntnissen die Diskussionen dominieren.</p>
      <h2>Warum Sprache wichtiger ist, als wir anerkennen</h2>
      <p>Sprache ist nicht nur ein Kommunikationsmittel. Sie ist eine Denkstruktur, ein Kulturbehälter und ein Machtmechanismus. Wenn man alle Teilnehmenden dazu zwingt, in einer Sprache zu operieren, die für manche Muttersprache und für andere Fremdsprache ist, schafft man systematische Benachteiligung.</p>
      <blockquote>Wenn man eine Aktivität gestaltet, die Teilnehmende ohne eine gemeinsame Sprache kommunizieren lässt — mit Geste, Bild, Bewegung, Klang — entdeckt man, was interkulturelle Kommunikation wirklich ist: nicht der fließende Austausch von Worten, sondern die kreative Aushandlung von Bedeutung.</blockquote>
      <h2>Mehrsprachigkeit und Beschäftigungsfähigkeit</h2>
      <p>Jenseits der ethischen und pädagogischen Dimensionen ist Mehrsprachigkeit ein zunehmend wertvolles Arbeitsmarktgut. Junge Menschen, die in mehreren Sprachen bedeutungsvoll kommunizieren können, werden von Arbeitgebern in allen Sektoren gesucht.</p>
"""
},
'20': {
'title_tr': "Küresel Çağda Kültürel Kimlik: Genç Avrupalıların 2025'te Söyledikleri",
'title_de': "Kulturelle Identität im globalen Zeitalter: Was junge Europäer 2025 sagen",
'content_tr': """
      <p>Yalova'daki bir gence kimliğinin ne olduğunu sorun; büyük ihtimalle sorunun davet ettiğinden daha karmaşık bir yanıt alırsınız. Türk, evet — ama aynı zamanda Avrupalı, K-pop hayranı, Alman futbol kulübü taraftarı ve küresel ölçekte iletişim kuran, kültürel kimliğini katmanlı, tartışmalı ve sürekli değişen bir nesil üyesi.</p>
      <h2>Eski Model Çözülüyor</h2>
      <p>Yirminci yüzyılın büyük bölümünde siyasi düşünceye hâkim olan kültürel kimlik modeli, kültürlerin sınırlı, tutarlı ve görece istikrarlı olduğunu varsayıyordu. 2025'teki gençler kültürel kimliklerini çok farklı biçimde deneyimliyor.</p>
      <blockquote>Türk'üm, ama Amerikan filmleri izleyerek, İngiliz müziği dinleyerek, Alman felsefesi okuyarak büyüdüm; akşamlarımı Polonya ve Yunanistan'daki arkadaşlarımla konuşarak geçiriyorum. Kimliğim bir çelişki değil. Bir bileşim.</blockquote>
      <h2>Aidiyet ve Açıklık Arasında</h2>
      <p>Avrupa genelinde gençlerin kültürel kimliği üzerine yapılan araştırmalar tutarlı biçimde iki şeyi ortaya koyuyor: gençlerin yerel ve ulusal aidiyet duygusu güçlü, ve aynı zamanda kültürel farklılığa son derece açıklar. Bunları zıtlar olarak deneyimlemiyorlar.</p>
      <h2>Gençlik Değişiminin Rolü</h2>
      <p>Gençlik değişimleri bu süreci hızlandırır ve derinleştirir. Beş farklı ülkeden gençlerle iki ya da üç hafta geçirmek — birlikte yemek yemek, tartışmak, yaşam alanı paylaşmak — medyadan veya ders kitaplarından öğrenilebilecek her şeyden niteliksel olarak farklı bir kültürel farklılık deneyimi yaratır.</p>
""",
'content_de': """
      <p>Fragen Sie einen jungen Menschen in Yalova, was seine Identität ist, und Sie erhalten wahrscheinlich eine komplexere Antwort, als die Frage zu suggerieren scheint. Türkisch, ja — aber auch europäisch, auch K-Pop-Fan, auch Anhänger eines deutschen Fußballclubs, auch Teil einer Generation, die global kommuniziert.</p>
      <h2>Das alte Modell zerbricht</h2>
      <p>Das Modell kultureller Identität, das den Großteil des politischen Denkens im zwanzigsten Jahrhundert dominierte, nahm an, dass Kulturen begrenzt, kohärent und relativ stabil seien. Junge Menschen im Jahr 2025 erleben ihre kulturelle Identität sehr anders.</p>
      <blockquote>Ich bin türkisch, aber ich bin mit amerikanischen Filmen aufgewachsen, britische Musik hörend, deutsche Philosophie studierend und meine Abende damit verbringend, mit Freunden in Polen und Griechenland zu reden. Meine Identität ist kein Widerspruch. Sie ist ein Kompositum.</blockquote>
      <h2>Zwischen Zugehörigkeit und Offenheit</h2>
      <p>Forschung zur kulturellen Identität junger Menschen in ganz Europa zeigt konsistent zwei Dinge: Junge Menschen haben ein starkes Gefühl lokaler und nationaler Zugehörigkeit, und sie sind gleichzeitig tief offen für kulturelle Unterschiede.</p>
      <h2>Die Rolle des Jugendaustauschs</h2>
      <p>Jugendbegegnungen beschleunigen und vertiefen diesen Prozess. Zwei oder drei Wochen mit jungen Menschen aus fünf verschiedenen Ländern zu verbringen — gemeinsam zu essen, zu streiten, Lebensraum zu teilen — schafft ein gelebtes Erlebnis kultureller Unterschiede, das qualitativ anders ist als alles, was man aus Medien oder Lehrbüchern lernen kann.</p>
"""
},
'21': {
'title_tr': "Yapay Zeka Araçları Gençlik Çalışma Pratiğini Nasıl Dönüştürüyor",
'title_de': "Wie KI-Tools die Jugendarbeitspraxis transformieren",
'content_tr': """
      <p>Erişilebilir, güçlü yapay zeka araçlarının gelmesi neredeyse her alanda profesyonel pratikte en önemli gelişmelerden biri oldu. Gençlik çalışması istisna değil. Program tasarımından hibe yazımına, katılımcı iletişiminden etki değerlendirmesine kadar yapay zeka araçları gençlik kuruluşlarının çalışma biçimini değiştiriyor.</p>
      <h2>Yapay Zeka Araçlarının Fark Yaratmaya Başladığı Yerler</h2>
      <p>En anlık etki, zaman alıcı ve kalıplaşmış görevlerdeydi. Hibe yazımı bariz örnek: Yapay zeka araçları teklif bölümlerini taslak haline getirebilir, mantık çerçeveleri yapılandırabilir, değerlendirme metodolojileri önerebilir.</p>
      <blockquote>Risk, yapay zekanın gençlik çalışanlarını değiştirmesi değil. Risk, yapay zekayı etkili biçimde kullanmayı bilmeyen gençlik çalışanlarının bunu yapan gençlik çalışanları tarafından değiştirilmesidir.</blockquote>
      <h2>Program Tasarımı ve Değerlendirme</h2>
      <p>Yapay zeka araçları program tasarımı için giderek daha kullanışlı hale geliyor — oturum planları oluşturma, kolaylaştırma yöntemleri önerme, materyalleri farklı kitlelere uyarlama ve değerlendirme araçları oluşturma. Değerlendirme için ise nitel verileri kodlamaya, büyük veri kümelerindeki desenleri belirlemeye ve özet raporlar oluşturmaya yardımcı olabilirler.</p>
      <h2>Etik Boyutlar</h2>
      <ul>
        <li>Açık rıza ve uygun veri işleme anlaşmaları olmadan katılımcı kişisel verilerini üçüncü taraf yapay zeka araçlarına asla girmeyin</li>
        <li>Programlarınızda yapay zeka tarafından oluşturulan içerik kullandığınızda gençlerle şeffaf olun</li>
        <li>Tüm yapay zeka tarafından oluşturulan materyalleri dikkatlice inceleyin</li>
        <li>İnsan uzmanlığını amplify etmek için yapay zeka araçlarını kullanın, onun yerine geçmek için değil</li>
      </ul>
""",
'content_de': """
      <p>Das Aufkommen zugänglicher, leistungsstarker KI-Tools war eine der bedeutendsten Entwicklungen in der professionellen Praxis in fast jedem Bereich. Jugendarbeit ist keine Ausnahme. Von Programmdesign über Förderanträge bis hin zu Teilnehmerkommunikation und Wirkungsevaluation verändern KI-Tools die Arbeitsweise von Jugendorganisationen.</p>
      <h2>Wo KI-Tools bereits einen Unterschied machen</h2>
      <p>Die unmittelbarste Wirkung entfiel auf zeitaufwändige und formelhafte Aufgaben. Förderanträge sind das offensichtliche Beispiel: KI-Tools können Antragsabschnitte entwerfen, Logikrahmen strukturieren und Evaluierungsmethodologien vorschlagen.</p>
      <blockquote>Das Risiko ist nicht, dass KI Jugendfachkräfte ersetzen wird. Das Risiko ist, dass Jugendfachkräfte, die nicht verstehen, wie man KI effektiv einsetzt, durch Jugendfachkräfte ersetzt werden, die es tun.</blockquote>
      <h2>Programmdesign und Evaluation</h2>
      <p>KI-Tools sind zunehmend nützlich für Programmdesign — Sitzungspläne generieren, Facilitierungsmethoden vorschlagen, Materialien für verschiedene Zielgruppen anpassen und Evaluierungsinstrumente erstellen. Für die Evaluation können sie bei der Kodierung qualitativer Daten, der Identifizierung von Mustern und der Erstellung von Zusammenfassungsberichten helfen.</p>
      <h2>Ethische Dimensionen</h2>
      <ul>
        <li>Niemals persönliche Daten von Teilnehmenden ohne ausdrückliche Einwilligung in Drittanbieter-KI-Tools eingeben</li>
        <li>Mit jungen Menschen transparent sein, wenn KI-generierte Inhalte in Programmen verwendet werden</li>
        <li>Alle KI-generierten Materialien sorgfältig überprüfen</li>
        <li>KI-Tools nutzen, um menschliche Expertise zu verstärken, nicht zu ersetzen</li>
      </ul>
"""
},
'22': {
'title_tr': "Deepfake'ler, Dezenformasyon ve Demokrasi: Gençlik Çalışanlarının Bilmesi Gerekenler",
'title_de': "Deepfakes, Desinformation und Demokratie: Was Jugendfachkräfte wissen müssen",
'content_tr': """
      <p>2024 seçim döngüsü, analistler tarafından "tarihin en dezinformasyon dolu seçim yılı" olarak nitelendirildi. Dört milyarı aşkın insan dünya genelinde ulusal seçimlerde oy kullandı. Yapay zeka tarafından oluşturulan dezenformasyon — sahte videolar, uydurma alıntılar, yapay haberler — düzinelerce ülkede siyasi bir silah olarak kullanıldı.</p>
      <h2>Deepfake Nedir ve Nasıl Çalışır</h2>
      <p>Deepfake, gerçekleşmemiş bir şeyi tasvir etmek için yapay zeka tarafından oluşturulan bir video, ses kaydı veya görüntüdür. Bu teknoloji, eğitimli gözlemciler için bile gerçek kayıtlardan giderek ayırt edilemez hale gelen sentetik medya oluşturmak için derin öğrenme kullanır.</p>
      <blockquote>Çoğu siyasi dezenformasyonun amacı insanları belirli yalanlar konusunda ikna etmek değildir. Gerçeğin belirlenemez olduğuna dair genelleşmiş bir his yaratmaktır — herkesin yalan söylediği, tüm kaynakların eşit derecede güvenilmez olduğu hissi. Epistemik felç, başlı başına bir siyasi çıktıdır.</blockquote>
      <h2>Gençlik Çalışanları Ne Yapabilir</h2>
      <ul>
        <li><strong>Yanal okuma</strong> öğretin: bir kaynağı izole olarak değerlendirmek yerine, diğer kaynakların o kaynak hakkında ne söylediğini kontrol etmek</li>
        <li><strong>Duygusal düzenleme</strong> pratiği yapın: öfke veya iğrenme uyandırmak için tasarlanmış içerik dezinformasyona daha yatkındır</li>
        <li><strong>Doğrulama araçları</strong> kullanın: ters görsel arama, video doğrulama için InVID/WeVerify</li>
        <li><strong>Kaynak üçgenleme</strong> alışkanlıkları geliştirin: bu iddia birden fazla bağımsız kaynakta yer alıyor mu?</li>
      </ul>
""",
'content_de': """
      <p>Der Wahlzyklus 2024 wurde von Analysten als „das am stärksten informationsgestörte Wahljahr der Geschichte" bezeichnet. Mehr als vier Milliarden Menschen wählten in nationalen Wahlen auf der ganzen Welt. KI-generierte Desinformation — gefälschte Videos, fabrizierte Zitate, synthetische Nachrichten — wurde in Dutzenden von Ländern als politische Waffe eingesetzt.</p>
      <h2>Was Deepfakes sind und wie sie funktionieren</h2>
      <p>Ein Deepfake ist ein Video, eine Audioaufnahme oder ein Bild, das von künstlicher Intelligenz erstellt wurde, um etwas darzustellen, das nicht passiert ist. Die Technologie verwendet Deep Learning, um synthetische Medien zu erstellen, die selbst für geschulte Beobachter zunehmend nicht von echten Aufnahmen zu unterscheiden sind.</p>
      <blockquote>Das Ziel vieler politischer Desinformation ist nicht, Menschen von spezifischen Unwahrheiten zu überzeugen. Es ist, ein verallgemeinertes Gefühl zu erzeugen, dass Wahrheit unmöglich zu bestimmen ist. Epistemische Lähmung ist selbst ein politisches Ergebnis.</blockquote>
      <h2>Was Jugendfachkräfte tun können</h2>
      <ul>
        <li><strong>Laterales Lesen</strong> lehren: überprüfen, was andere Quellen über eine Quelle sagen, anstatt sie isoliert zu bewerten</li>
        <li><strong>Emotionale Regulation</strong> üben: Inhalte, die Wut oder Ekel provozieren, sind eher Desinformation</li>
        <li><strong>Verifikationstools</strong> nutzen: umgekehrte Bildsuche, InVID/WeVerify für Video-Verifikation</li>
        <li><strong>Quellen-Triangulation</strong> entwickeln: erscheint diese Behauptung in mehreren unabhängigen zuverlässigen Quellen?</li>
      </ul>
"""
},
'23': {
'title_tr': "Algoritma ve Genç İnsan: Sosyal Medyanın Gizli Mimarisi",
'title_de': "Der Algorithmus und der junge Mensch: Die versteckte Architektur der sozialen Medien",
'content_tr': """
      <p>Gençler ortalama günde 4-6 saat sosyal medya platformlarında vakit geçiriyor. Çoğunun bu platformların ne gördüklerini, neden gördüklerini ve bu seçim sürecinin neyi başarmak için tasarlandığını nasıl belirlediği konusunda neredeyse hiç anlayışı yok. Bu cehalet tesadüfi değil; iş modeli buna bağlı olan platformların bilinçli bir tasarım tercihi.</p>
      <h2>Öneri Algoritmaları Nasıl Çalışır</h2>
      <p>Öneri algoritması her büyük sosyal medya platformunun motorudur. Hangi gönderilerin akışınızda görüneceğine, hangi videoların otomatik oynanacağına, hangi hesapların size önerileceğine karar verir. Hedefi — her durumda — "etkileşimi" en üst düzeye çıkarmaktır: platformda geçirdiğiniz süre, yaptığınız eylemler, oluşturduğunuz içerik.</p>
      <blockquote>Algoritma kimseyi radikalize etmeye niyet etmez. Sadece zaten tükettiğinizden biraz daha aşırı içeriğin dikkatinizi daha fazla çekeceğini biliyor. Bunu yüzlerce kez tekrarlayın ve birikimli etki derin olabilir.</blockquote>
      <h2>Filtre Balonları ve Yankı Odaları</h2>
      <p>Öneri algoritmaları ayrıca filtre balonları oluşturur: ağırlıklı olarak mevcut inançlarınızı doğrulayan görüşlerle karşılaştığınız bilgi ortamları. Bunun sonucu, farklı algoritmik balonlardaki insanların gerçekten farklı bilgi gerçekliklerinde yaşamasıdır.</p>
      <h2>Gençlerin Anlaması Gerekenler</h2>
      <ul>
        <li>Gençlere kendi algoritmalarını denetlemeyi öğretin: onlara ne gösteriyor? Neyi gizliyor?</li>
        <li>Kasıtlı medya tüketimi pratiği yapın: algoritmanın sunduklarını almak yerine ne tüketeceğini seçmek</li>
        <li>Kronolojik akışlar kullanın: size en fazla etkileşim sağlayacak içeriği değil, takip etmeyi seçtiklerinizi gösterir</li>
        <li>Düzenli molalar verin ve ruh halinizin ve dünya görüşünüzün nasıl değiştiğini fark edin</li>
      </ul>
""",
'content_de': """
      <p>Junge Menschen verbringen täglich durchschnittlich 4-6 Stunden auf Social-Media-Plattformen. Die meisten von ihnen haben kaum Verständnis davon, wie diese Plattformen entscheiden, was sie sehen, warum sie es sehen und was dieser Auswahlprozess erreichen soll. Diese Unwissenheit ist nicht zufällig. Sie ist eine bewusste Designentscheidung von Plattformen, deren Geschäftsmodell davon abhängt.</p>
      <h2>Wie Empfehlungsalgorithmen funktionieren</h2>
      <p>Der Empfehlungsalgorithmus ist der Motor jeder großen Social-Media-Plattform. Er entscheidet, welche Beiträge in Ihrem Feed erscheinen, welche Videos automatisch abspielen, welche Konten Ihnen vorgeschlagen werden. Sein Ziel — in jedem Fall — ist es, „Engagement" zu maximieren.</p>
      <blockquote>Der Algorithmus beabsichtigt nicht, jemanden zu radikalisieren. Er weiß nur, dass Inhalte, die etwas extremer sind als das, was Sie bereits konsumiert haben, eher Ihre Aufmerksamkeit halten. Wiederholen Sie dies hunderte Male, und der kumulative Effekt kann tiefgreifend sein.</blockquote>
      <h2>Filterblasen und Echokammern</h2>
      <p>Empfehlungsalgorithmen schaffen auch Filterblasen: Informationsumgebungen, in denen man hauptsächlich Ansichten begegnet, die die eigenen bestehenden Überzeugungen bestätigen. Das Ergebnis ist, dass Menschen in verschiedenen algorithmischen Blasen wirklich unterschiedliche Informationsrealitäten bewohnen.</p>
      <h2>Was junge Menschen verstehen müssen</h2>
      <ul>
        <li>Jungen Menschen beibringen, ihren eigenen Algorithmus zu prüfen: Was zeigt er ihnen? Was verbirgt er?</li>
        <li>Bewussten Medienkonsum üben: wählen, was man konsumiert, anstatt zu empfangen, was der Algorithmus serviert</li>
        <li>Chronologische Feeds nutzen, wo verfügbar</li>
        <li>Regelmäßige Pausen einlegen und bemerken, wie sich Stimmung und Weltbild verändern</li>
      </ul>
"""
},
}

def add_translations(filepath, trans_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for art_id, trans in trans_dict.items():
        insert = ""
        for key, val in trans.items():
            safe_val = val.replace('`', "'")
            insert += f",\n    {key}: `{safe_val}`"

        pattern = rf"(  '{art_id}': {{.*?content: `.*?`)"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            end = match.end()
            after_chunk = content[end:end+100]
            if 'content_tr' not in content[match.start():end+20]:
                content = content[:end] + insert + content[end:]
                print(f"  ✓ Article {art_id}")
            else:
                print(f"  ~ Article {art_id} already done")
        else:
            print(f"  ✗ Article {art_id} not found")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'js', 'data', 'articles.js')
    add_translations(filepath, TRANS)
    print("Done.")
