const fs = require('fs');

const en = {
  /* NAV */
  'nav.home': 'Home', 'nav.about': 'About', 'nav.focus': 'Focus Areas',
  'nav.projects': 'Projects', 'nav.partnership': 'Partnerships',
  'nav.impact': 'Impact', 'nav.blog': 'Insights', 'nav.team': 'Team',
  'nav.contact': 'Contact', 'nav.join': 'Join Us',

  /* HERO */
  'hero.badge': 'European Youth Network · Est. 2026',
  'hero.title1': 'Connecting', 'hero.title2': 'youth,',
  'hero.title3': 'culture &', 'hero.title4': 'action.',
  'hero.sub': 'YouthTICK is a contemporary youth network empowering young people through international collaboration, innovation and cultural interaction.',
  'hero.cta1': 'Explore Projects', 'hero.cta2': 'Become a Volunteer', 'hero.cta3': 'Partner With Us',
  'hero.trust': 'Active in 5 countries · 120+ youth participants',
  'hero.badge1.num': '5', 'hero.badge1.label': 'Countries',
  'hero.badge2.num': 'Erasmus+', 'hero.badge2.label': 'Partner',

  /* TRUST BAR */
  'trust.label': 'Supported by & collaborating with',

  /* ABOUT TEASER (Home) */
  'about.label': 'Who We Are', 'about.title': 'A new kind of youth organization.',
  'about.p1': 'YouthTICK operates at the intersection of international mobility, civic participation and entrepreneurial thinking — creating spaces where young people don\'t just participate, they lead.',
  'about.p2': 'From Berlin to Istanbul, from Erasmus+ exchanges to grassroots innovation labs, we build ecosystems that turn ambition into action.',
  'about.cta': 'Our Story',

  /* STATS (Home & Impact) */
  'stat1.label': 'Active projects in 2026', 'stat2.label': 'Youth participants',
  'stat3.label': 'Countries active', 'stat4.label': 'Partner organisations',

  /* FOCUS (Home & Focus Page) */
  'focus.label': 'What We Do', 'focus.title': 'Six pillars of youth action.',
  'focus.all': 'View all areas →',
  'focus.f1.title': 'Erasmus+ Projects', 'focus.f1.desc': 'Youth exchanges, training courses and strategic partnerships across Europe.',
  'focus.f2.title': 'Youth Participation', 'focus.f2.desc': 'Civic engagement, democratic processes and active citizenship programs.',
  'focus.f3.title': 'Entrepreneurship', 'focus.f3.desc': 'Innovation labs, startup mentorship and social entrepreneurship accelerators.',
  'focus.f4.title': 'Cultural Interaction', 'focus.f4.desc': 'Intercultural dialogue, arts, heritage and creative exchange programs.',
  'focus.f5.title': 'Research & Reports', 'focus.f5.desc': 'Data-driven youth research, policy papers and impact measurement.',
  'focus.f6.title': 'International Networking', 'focus.f6.desc': 'Cross-border partnerships, NGO coalitions and global youth forums.',

  /* PROJECTS */
  'proj.label': 'Recent Work', 'proj.title': 'Featured projects.', 'proj.all': 'All Projects →',
  'proj.page.title': 'Projects & Initiatives', 'proj.page.sub': 'From local innovation to European networks. Here is what we are building.',
  'proj.active': 'Active Projects', 'proj.past': 'Past Projects',

  /* PULLQUOTE */
  'quote.text': 'YouthTICK gave me a platform I didn\'t know I needed — to connect, to build, to lead.',
  'quote.author': 'Mia Schneider', 'quote.role': 'Youth Exchange Participant · Berlin, Germany',

  /* BLOG */
  'blog.label': 'Insights', 'blog.title': 'Stories, research and updates from the network.',
  'blog.all': 'All Articles →',

  /* CTA BANNER */
  'cta.title': 'Ready to be part of something bigger?',
  'cta.sub': 'Join a network of 120+ young changemakers from 5 countries.',
  'cta.btn1': 'Join as Volunteer', 'cta.btn2': 'Get in Touch',

  /* FOOTER */
  'footer.tagline': 'A contemporary European youth network empowering young people through international collaboration, innovation and cultural interaction.',
  'footer.copy': '© 2026 YouthTICK. All rights reserved.',
  'footer.connect': 'Connect', 'footer.community': 'Community', 'footer.platform': 'Platform',

  /* ABOUT PAGE */
  'about.page.title': 'About YouthTICK',
  'about.mission.title': 'Mission', 'about.mission.text': 'To empower young people with tools, networks and opportunities to shape their own futures and contribute meaningfully to European society.',
  'about.vision.title': 'Vision', 'about.vision.text': 'A Europe where every young person—regardless of background—has an equal voice, equal opportunity and equal agency to lead change.',
  'about.lead': '"We don\'t run programs for youth. We build infrastructure with youth."',
  'about.m1': 'YouthTICK was born from a simple but radical conviction: that young people are not the leaders of tomorrow — they are the leaders of today. We exist to make that belief operational, not rhetorical.',
  'about.m2': 'Founded in 2026 at the intersection of Berlin\'s creative ecosystem and Istanbul\'s entrepreneurial energy, YouthTICK is a new-generation youth network building across 5 countries. We design experiences — exchanges, labs, forums, training courses — built around the actual ambitions of young people, not institutional agendas.',
  'about.m3': 'Our work spans Erasmus+ project management, civic education, cultural programming and social entrepreneurship. What connects it all is a commitment to meaningful participation — not tokenism, not checkbox inclusion, but genuine co-creation.',
  'about.m4': 'We are actively building our Erasmus+ recognition and partnership networks. We collaborate with SALTO, JUGEND für Europa and Youth Forum Jeunesse. What we are most proud of is the 120+ young people already engaged in our 2026 programs and the pipeline of ambitious projects ahead.',
  
  'about.values.label': 'What We Stand For', 'about.values.title': 'Six values that drive everything we do.',
  'about.v1.title': 'Agency over participation', 'about.v1.desc': 'We design for decision-making power, not just inclusion. Young people shape our programs, not just attend them.',
  'about.v2.title': 'Openness as infrastructure', 'about.v2.desc': 'All our methodologies, toolkits and reports are open-source by default. Knowledge should compound, not be hoarded.',
  'about.v3.title': 'Impact before optics', 'about.v3.desc': 'We measure outcomes, not outputs. Depth of transformation beats width of reach in everything we do.',
  'about.v4.title': 'Cultural humility', 'about.v4.desc': 'We operate across multiple cultures and know that no single model fits all. We adapt, listen and iterate constantly.',
  'about.v5.title': 'Radical collaboration', 'about.v5.desc': 'The most complex youth challenges require NGOs, governments, startups and universities at the same table.',
  'about.v6.title': 'Sustainability at the core', 'about.v6.desc': 'Environmental, social and institutional sustainability isn\'t a focus area — it\'s a lens applied to everything we do.',

  'about.journey.label': 'Our Journey', 'about.journey.title': 'Our journey — from idea to network.',
  'about.j1.date': 'Q1 2026', 'about.j1.text': 'YouthTICK founded in Berlin. Core team assembled from Germany and Turkey. First partnership agreements signed.',
  'about.j2.date': 'Q2 2026', 'about.j2.text': 'First youth exchange launched between Germany and Turkey. 40 participants. Erasmus+ application submitted.',
  'about.j3.date': 'Q3 2026', 'about.j3.text': 'Second project launched. Innovation Lab pilot program begins in Berlin. 80+ youth participants reached.',
  'about.j4.date': 'H2 2026 — Planned', 'about.j4.text': '3+ active projects, 5 countries, 120+ participants. First annual report to be published. Erasmus+ accreditation in progress.',

  /* IMPACT PAGE */
  'impact.label': 'Our Impact', 'impact.title': 'A new generation of measurable change.', 'impact.sub': 'Every number represents a real person, a real project, a real transformation. Here is the evidence.',
  'impact.yy.label': 'Year by Year', 'impact.yy.title': 'Growth across every dimension.',
  'impact.yy.launch': 'Project launched', 'impact.yy.part': 'Participants', 'impact.yy.country': 'Countries', 'impact.yy.active': 'Projects active', 'impact.yy.proj': 'Projects',
  
  'impact.sdg.title': 'Contributing to global goals.',
  'impact.sdg1': 'SDG 4 — Quality Education', 'impact.sdg1.desc': 'Non-formal learning, skill development and lifelong education access for all young people.',
  'impact.sdg2': 'SDG 10 — Reduced Inequalities', 'impact.sdg2.desc': 'Creating equal opportunity for youth regardless of geographic or socioeconomic background.',
  'impact.sdg3': 'SDG 13 — Climate Action', 'impact.sdg3.desc': 'Building the next generation of environmental advocates and sustainability practitioners.',
  'impact.sdg4': 'SDG 17 — Partnerships', 'impact.sdg4.desc': 'Transnational collaboration as the cornerstone of every program we design and deliver.',
  'impact.sdg5': 'SDG 11 — Sustainable Cities', 'impact.sdg5.desc': 'Youth-led urban innovation programs shaping more liveable, inclusive cities across Europe.',
  'impact.sdg6': 'SDG 16 — Peace & Institutions', 'impact.sdg6.desc': 'Civic education, democratic participation and intercultural dialogue as foundations of peace.',
  'impact.sdg7': 'SDG 8 — Decent Work', 'impact.sdg7.desc': 'Youth entrepreneurship programs creating sustainable economic pathways for young people.',
  'impact.sdg8': 'SDG 5 — Gender Equality', 'impact.sdg8.desc': 'All programs designed with gender equity as a core principle, not an afterthought.',

  'impact.rep.title': 'Our research, freely available.',
  'impact.rep1.date': '2026 — Coming Soon', 'impact.rep1.title': 'YouthTICK Founding Report: Youth Participation in South-East Europe 2026', 'impact.rep1.meta': 'Expected: Q4 2026 · Available in EN, TR, DE',
  'impact.rep2.date': '2026 — In Progress', 'impact.rep2.title': 'Germany–Turkey Youth Mobility: Landscape & Opportunities', 'impact.rep2.meta': 'Draft · Co-authored with JUGEND für Europa · Expected Q3 2026',
  'impact.rep.notify': 'Get Notified', 'impact.rep.collab': 'Collaborate →',

  /* PARTNERSHIPS PAGE */
  'part.title': 'Build with us.', 'part.sub': 'The most complex youth challenges require radical collaboration. We partner with NGOs, universities, municipalities and progressive companies to create scalable impact.',
  'part.net.label': 'Our Network', 'part.net.title': 'Global reach, local roots.',
  'part.join.label': 'Become a Partner', 'part.join.title': 'Let\'s build the next generation of youth programs.',
  'part.join.sub': 'Whether you are an NGO looking for a reliable Erasmus+ partner, or a municipality wanting to engage youth, we bring the expertise, network and energy to make it happen.',
  'part.t1': 'Erasmus+ Consortium', 'part.t1.desc': 'Looking for a reliable partner in Germany or Turkey? We specialize in KA1 mobility and KA2 strategic partnerships.',
  'part.t2': 'Research & Data', 'part.t2.desc': 'We collaborate with universities and think tanks to conduct field research on youth trends and policy.',
  'part.t3': 'Corporate CSR', 'part.t3.desc': 'Align your social responsibility goals with high-impact youth entrepreneurship and sustainability programs.',
  'part.t4': 'Local Implementation', 'part.t4.desc': 'We help municipalities and local governments design youth-friendly policies and participatory spaces.',
  'part.cta.title': 'Ready to collaborate? Let\'s talk.',

  /* TEAM PAGE */
  'team.label': 'Our Team', 'team.title': 'The people behind the network.', 'team.sub': 'A diverse group of youth workers, researchers, designers and strategists working across Europe to empower the next generation.',
  'team.r1': 'Co-Founder & Director', 'team.r2': 'Head of Programs (DE)', 'team.r3': 'Erasmus+ Coordinator', 'team.r4': 'Community Manager',
  'team.r5': 'Research Lead', 'team.r6': 'Creative Director', 'team.r7': 'Partnerships (TR)', 'team.r8': 'Youth Advocate',
  'team.open.title': 'Join the Core Team', 'team.open.desc': 'We are always looking for passionate youth workers, grant writers and project managers to join our growing network.', 'team.open.btn': 'View Open Roles',

  /* CONTACT PAGE */
  'contact.label': 'Contact', 'contact.title': 'Get in touch.', 'contact.sub': 'Have a project idea? Want to partner? Or just want to say hi? Drop us a message and we will get back to you within 48 hours.',
  'contact.office': 'Offices', 'contact.off1': 'Berlin, Germany', 'contact.off2': 'Istanbul, Turkey',
  'contact.form.name': 'Your Name', 'contact.form.email': 'Email Address', 'contact.form.subject': 'Subject', 'contact.form.msg': 'Your Message', 'contact.form.send': 'Send Message',
  'contact.form.success': 'Message sent successfully! We will get back to you soon.',

  /* VOLUNTEER PAGE */
  'vol.label': 'Volunteer', 'vol.title': 'Shape the ecosystem.', 'vol.sub': 'We don\'t just want your time. We want your ideas. Join our network of 120+ young changemakers and help us build the future of youth work.',
  'vol.w1.title': 'Lead Projects', 'vol.w1.desc': 'Don\'t just assist. Take ownership of local initiatives and international youth exchanges.',
  'vol.w2.title': 'Build Your Network', 'vol.w2.desc': 'Connect with NGOs, activists and entrepreneurs across 5+ European countries.',
  'vol.w3.title': 'Learn by Doing', 'vol.w3.desc': 'Gain hands-on experience in project management, grant writing and event production.',
  'vol.form.title': 'Volunteer Application',
  'vol.form.area': 'Area of Interest', 'vol.form.a1': 'Event Organization', 'vol.form.a2': 'Content & Media', 'vol.form.a3': 'Project Writing (Erasmus+)', 'vol.form.a4': 'Research & Data',
  'vol.form.mot': 'Why do you want to join YouthTICK?', 'vol.form.submit': 'Submit Application'
};

const tr = {
  /* NAV */
  'nav.home': 'Ana Sayfa', 'nav.about': 'Hakkımızda', 'nav.focus': 'Odak Alanları',
  'nav.projects': 'Projeler', 'nav.partnership': 'Ortaklıklar',
  'nav.impact': 'Etki', 'nav.blog': 'İçgörüler', 'nav.team': 'Ekip',
  'nav.contact': 'İletişim', 'nav.join': 'Katıl',

  /* HERO */
  'hero.badge': 'Avrupa Gençlik Ağı · Kur. 2026',
  'hero.title1': 'Gençliği,', 'hero.title2': 'kültürü',
  'hero.title3': 've eylemi', 'hero.title4': 'buluşturuyoruz.',
  'hero.sub': 'YouthTICK; uluslararası işbirliği, inovasyon ve kültürel etkileşim aracılığıyla gençleri güçlendiren modern bir gençlik ağıdır.',
  'hero.cta1': 'Projeleri Keşfet', 'hero.cta2': 'Gönüllü Ol', 'hero.cta3': 'Ortak Ol',
  'hero.trust': '5 ülkede aktif · 120+ gençlik katılımcısı',
  'hero.badge1.num': '5', 'hero.badge1.label': 'Ülke',
  'hero.badge2.num': 'Erasmus+', 'hero.badge2.label': 'Ortağı',

  /* TRUST BAR */
  'trust.label': 'Destekçilerimiz ve iş birliği yaptığımız kurumlar',

  /* ABOUT TEASER (Home) */
  'about.label': 'Biz Kimiz', 'about.title': 'Farklı bir gençlik organizasyonu.',
  'about.p1': 'YouthTICK; uluslararası hareketlilik, sivil katılım ve girişimcilik düşüncesinin kesişim noktasında faaliyet göstererek gençlerin sadece katılmadığı, liderlik ettiği alanlar yaratır.',
  'about.p2': 'Berlin\'den İstanbul\'a, Erasmus+ değişimlerinden tabandan inovasyon laboratuvarlarına kadar hırsı eyleme dönüştüren ekosistemler kuruyoruz.',
  'about.cta': 'Hikayemiz',

  /* STATS (Home & Impact) */
  'stat1.label': 'Devam eden proje (2026)', 'stat2.label': 'Gençlik katılımcısı',
  'stat3.label': 'Aktif ülke', 'stat4.label': 'Ortak kuruluş',

  /* FOCUS (Home & Focus Page) */
  'focus.label': 'Ne Yapıyoruz', 'focus.title': 'Gençlik eyleminin altı sütunu.',
  'focus.all': 'Tüm alanları gör →',
  'focus.f1.title': 'Erasmus+ Projeleri', 'focus.f1.desc': 'Avrupa genelinde gençlik değişimleri, eğitim kursları ve stratejik ortaklıklar.',
  'focus.f2.title': 'Gençlik Katılımı', 'focus.f2.desc': 'Sivil katılım, demokratik süreçler ve aktif vatandaşlık programları.',
  'focus.f3.title': 'Girişimcilik', 'focus.f3.desc': 'İnovasyon laboratuvarları, startup mentörlüğü ve sosyal girişimcilik hızlandırıcıları.',
  'focus.f4.title': 'Kültürel Etkileşim', 'focus.f4.desc': 'Kültürlerarası diyalog, sanat, miras ve yaratıcı değişim programları.',
  'focus.f5.title': 'Araştırma & Raporlar', 'focus.f5.desc': 'Veriye dayalı gençlik araştırması, politika belgeleri ve etki ölçümü.',
  'focus.f6.title': 'Uluslararası Ağ', 'focus.f6.desc': 'Sınır ötesi ortaklıklar, STK koalisyonları ve küresel gençlik forumları.',

  /* PROJECTS */
  'proj.label': 'Son Çalışmalarımız', 'proj.title': 'Öne çıkan projeler.', 'proj.all': 'Tüm Projeler →',
  'proj.page.title': 'Projeler & Girişimler', 'proj.page.sub': 'Yerel inovasyondan Avrupa ağlarına. İşte inşa ettiklerimiz.',
  'proj.active': 'Aktif Projeler', 'proj.past': 'Geçmiş Projeler',

  /* PULLQUOTE */
  'quote.text': 'YouthTICK bana ihtiyaç duyduğumu bilmediğim bir platform sundu — bağlanmak, inşa etmek, liderlik etmek için.',
  'quote.author': 'Mia Schneider', 'quote.role': 'Gençlik Değişimi Katılımcısı · Berlin, Almanya',

  /* BLOG */
  'blog.label': 'İçgörüler', 'blog.title': 'Ağdan hikayeler, araştırmalar ve güncellemeler.',
  'blog.all': 'Tüm Makaleler →',

  /* CTA BANNER */
  'cta.title': 'Daha büyük bir şeyin parçası olmaya hazır mısın?',
  'cta.sub': '5 ülkeden 120+ genç değişimciden oluşan bir ağa katıl.',
  'cta.btn1': 'Gönüllü Ol', 'cta.btn2': 'İletişime Geç',

  /* FOOTER */
  'footer.tagline': 'Uluslararası işbirliği, inovasyon ve kültürel etkileşim yoluyla gençleri güçlendiren modern bir Avrupa gençlik ağı.',
  'footer.copy': '© 2026 YouthTICK. Tüm hakları saklıdır.',
  'footer.connect': 'İletişim', 'footer.community': 'Topluluk', 'footer.platform': 'Platform',

  /* ABOUT PAGE */
  'about.page.title': 'YouthTICK Hakkında',
  'about.mission.title': 'Misyon', 'about.mission.text': 'Gençleri, kendi geleceklerini şekillendirmeleri ve Avrupa toplumuna anlamlı bir şekilde katkıda bulunmaları için araçlar, ağlar ve fırsatlarla güçlendirmek.',
  'about.vision.title': 'Vizyon', 'about.vision.text': 'Geçmişi ne olursa olsun her gencin eşit sese, eşit fırsata ve değişime öncülük edecek eşit güce sahip olduğu bir Avrupa.',
  'about.lead': '"Gençler için program yürütmüyoruz. Gençlerle birlikte altyapı inşa ediyoruz."',
  'about.m1': 'YouthTICK basit ama radikal bir inançtan doğdu: Gençler yarının liderleri değil — bugünün liderleridir. Biz bu inancı retorik olmaktan çıkarıp operasyonel hale getirmek için varız.',
  'about.m2': 'Berlin\'in yaratıcı ekosistemi ile İstanbul\'un girişimci enerjisinin kesişiminde 2026\'da kurulan YouthTICK, 5 ülkede yapılanan yeni nesil bir gençlik ağıdır. Kurumsal gündemler etrafında değil, gençlerin gerçek tutkuları etrafında şekillenen deneyimler (değişimler, laboratuvarlar, forumlar) tasarlıyoruz.',
  'about.m3': 'Çalışmalarımız Erasmus+ proje yönetimi, sivil eğitim, kültürel programlama ve sosyal girişimciliği kapsıyor. Tüm bunları birleştiren şey ise anlamlı katılıma olan bağlılığımızdır — göstermelik dahil edilme değil, gerçek ortak yaratım.',
  'about.m4': 'Erasmus+ akreditasyonumuzu ve ortaklık ağlarımızı aktif olarak inşa ediyoruz. SALTO, JUGEND für Europa ve Youth Forum Jeunesse ile işbirliği yapıyoruz. En çok gurur duyduğumuz şey ise, 2026 programlarımıza şimdiden dahil olan 120+ genç ve önümüzdeki iddialı projelerimizdir.',
  
  'about.values.label': 'Neyi Savunuyoruz', 'about.values.title': 'Yaptığımız her şeye yön veren altı değer.',
  'about.v1.title': 'Katılım değil, Temsiliyet', 'about.v1.desc': 'Sadece dahil etmek için değil, karar verme gücü için tasarlıyoruz. Gençler programlarımıza sadece katılmaz, onları şekillendirir.',
  'about.v2.title': 'Altyapı olarak açıklık', 'about.v2.desc': 'Tüm metodolojilerimiz, araç kitlerimiz ve raporlarımız varsayılan olarak açık kaynaktır. Bilgi istiflenmemeli, çoğalmalıdır.',
  'about.v3.title': 'Görünümden önce etki', 'about.v3.desc': 'Çıktıları değil, sonuçları ölçüyoruz. Dönüşümün derinliği, her zaman erişimin genişliğinden üstündür.',
  'about.v4.title': 'Kültürel tevazu', 'about.v4.desc': 'Farklı kültürlerde faaliyet gösteriyoruz ve tek bir modelin herkese uymayacağını biliyoruz. Sürekli uyum sağlıyor, dinliyor ve yineliyoruz.',
  'about.v5.title': 'Radikal işbirliği', 'about.v5.desc': 'En karmaşık gençlik sorunları; STK\'ların, hükümetlerin, girişimlerin ve üniversitelerin aynı masada olmasını gerektirir.',
  'about.v6.title': 'Merkezde sürdürülebilirlik', 'about.v6.desc': 'Çevresel, sosyal ve kurumsal sürdürülebilirlik bir odak alanı değil — yaptığımız her şeye uyguladığımız bir mercektir.',

  'about.journey.label': 'Yolculuğumuz', 'about.journey.title': 'Yolculuğumuz — fikirden ağa.',
  'about.j1.date': '1. Çeyrek 2026', 'about.j1.text': 'YouthTICK Berlin\'de kuruldu. Almanya ve Türkiye\'den çekirdek ekip oluşturuldu. İlk ortaklık anlaşmaları imzalandı.',
  'about.j2.date': '2. Çeyrek 2026', 'about.j2.text': 'Almanya ve Türkiye arasında ilk gençlik değişimi başlatıldı. 40 katılımcı. Erasmus+ başvurusu yapıldı.',
  'about.j3.date': '3. Çeyrek 2026', 'about.j3.text': 'İkinci proje başlatıldı. Berlin\'de İnovasyon Laboratuvarı pilot programı başladı. 80+ genç katılımcıya ulaşıldı.',
  'about.j4.date': '2. Yarı 2026 — Planlanan', 'about.j4.text': '3+ aktif proje, 5 ülke, 120+ katılımcı. İlk yıllık rapor yayınlanacak. Erasmus+ akreditasyon süreci devam ediyor.',

  /* IMPACT PAGE */
  'impact.label': 'Etkimiz', 'impact.title': 'Yeni nesil ölçülebilir değişim.', 'impact.sub': 'Her sayı gerçek bir insanı, gerçek bir projeyi, gerçek bir dönüşümü temsil ediyor. İşte kanıtı.',
  'impact.yy.label': 'Yıldan Yıla', 'impact.yy.title': 'Her boyutta büyüme.',
  'impact.yy.launch': 'Başlatılan Proje', 'impact.yy.part': 'Katılımcı', 'impact.yy.country': 'Ülke', 'impact.yy.active': 'Aktif Proje', 'impact.yy.proj': 'Projeler',
  
  'impact.sdg.title': 'Küresel hedeflere katkı.',
  'impact.sdg1': 'SKA 4 — Nitelikli Eğitim', 'impact.sdg1.desc': 'Tüm gençler için yaygın öğrenme, beceri geliştirme ve yaşam boyu eğitime erişim.',
  'impact.sdg2': 'SKA 10 — Eşitsizliklerin Azaltılması', 'impact.sdg2.desc': 'Coğrafi veya sosyoekonomik geçmişe bakılmaksızın gençler için fırsat eşitliği yaratmak.',
  'impact.sdg3': 'SKA 13 — İklim Eylemi', 'impact.sdg3.desc': 'Çevre savunucuları ve sürdürülebilirlik uygulayıcılarının yeni neslini inşa etmek.',
  'impact.sdg4': 'SKA 17 — Amaçlar için Ortaklıklar', 'impact.sdg4.desc': 'Tasarladığımız ve sunduğumuz her programın temel taşı olarak ulusötesi işbirliği.',
  'impact.sdg5': 'SKA 11 — Sürdürülebilir Şehirler', 'impact.sdg5.desc': 'Avrupa çapında daha yaşanabilir, kapsayıcı şehirleri şekillendiren gençlik liderliğindeki kentsel inovasyon programları.',
  'impact.sdg6': 'SKA 16 — Barış ve Kurumlar', 'impact.sdg6.desc': 'Barışın temelleri olarak sivil eğitim, demokratik katılım ve kültürlerarası diyalog.',
  'impact.sdg7': 'SKA 8 — İnsana Yakışır İş', 'impact.sdg7.desc': 'Gençler için sürdürülebilir ekonomik yollar yaratan gençlik girişimciliği programları.',
  'impact.sdg8': 'SKA 5 — Toplumsal Cinsiyet Eşitliği', 'impact.sdg8.desc': 'Tüm programlar, sonradan akla gelen bir düşünce olarak değil, temel bir prensip olarak cinsiyet eşitliği ile tasarlanır.',

  'impact.rep.title': 'Ücretsiz araştırmalarımız.',
  'impact.rep1.date': '2026 — Çok Yakında', 'impact.rep1.title': 'YouthTICK Kuruluş Raporu: Güneydoğu Avrupa\'da Gençlik Katılımı 2026', 'impact.rep1.meta': 'Beklenen: 4. Çeyrek 2026 · EN, TR, DE dillerinde',
  'impact.rep2.date': '2026 — Devam Ediyor', 'impact.rep2.title': 'Almanya-Türkiye Gençlik Hareketliliği: Manzara ve Fırsatlar', 'impact.rep2.meta': 'Taslak · JUGEND für Europa ile ortak yazarlık · Beklenen 3. Çeyrek 2026',
  'impact.rep.notify': 'Haberdar Ol', 'impact.rep.collab': 'İşbirliği Yap →',

  /* PARTNERSHIPS PAGE */
  'part.title': 'Bizimle inşa edin.', 'part.sub': 'En karmaşık gençlik sorunları radikal bir işbirliği gerektirir. Ölçeklenebilir etki yaratmak için STK\'lar, üniversiteler, belediyeler ve ilerici şirketlerle ortaklık yapıyoruz.',
  'part.net.label': 'Ağımız', 'part.net.title': 'Küresel erişim, yerel kökler.',
  'part.join.label': 'Ortak Olun', 'part.join.title': 'Gençlik programlarının yeni neslini birlikte inşa edelim.',
  'part.join.sub': 'İster güvenilir bir Erasmus+ ortağı arayan bir STK olun, ister gençleri dahil etmek isteyen bir belediye; bunu gerçekleştirmek için uzmanlığı, ağı ve enerjiyi getiriyoruz.',
  'part.t1': 'Erasmus+ Konsorsiyumu', 'part.t1.desc': 'Almanya veya Türkiye\'de güvenilir bir ortak mı arıyorsunuz? KA1 hareketliliği ve KA2 stratejik ortaklıklarında uzmanız.',
  'part.t2': 'Araştırma ve Veri', 'part.t2.desc': 'Gençlik trendleri ve politikaları hakkında saha araştırmaları yürütmek için üniversiteler ve düşünce kuruluşlarıyla işbirliği yapıyoruz.',
  'part.t3': 'Kurumsal KSS', 'part.t3.desc': 'Sosyal sorumluluk hedeflerinizi yüksek etkili gençlik girişimciliği ve sürdürülebilirlik programlarıyla uyumlu hale getirin.',
  'part.t4': 'Yerel Uygulama', 'part.t4.desc': 'Belediyelerin ve yerel yönetimlerin genç dostu politikalar ve katılımcı alanlar tasarlamalarına yardımcı oluyoruz.',
  'part.cta.title': 'İşbirliğine hazır mısınız? Konuşalım.',

  /* TEAM PAGE */
  'team.label': 'Ekibimiz', 'team.title': 'Ağın arkasındaki insanlar.', 'team.sub': 'Yeni nesli güçlendirmek için Avrupa çapında çalışan gençlik çalışanları, araştırmacılar, tasarımcılar ve stratejistlerden oluşan çeşitli bir grup.',
  'team.r1': 'Kurucu Ortak & Direktör', 'team.r2': 'Programlar Başkanı (DE)', 'team.r3': 'Erasmus+ Koordinatörü', 'team.r4': 'Topluluk Yöneticisi',
  'team.r5': 'Araştırma Lideri', 'team.r6': 'Kreatif Direktör', 'team.r7': 'Ortaklıklar (TR)', 'team.r8': 'Gençlik Savunucusu',
  'team.open.title': 'Çekirdek Ekibe Katıl', 'team.open.desc': 'Büyüyen ağımıza katılacak tutkulu gençlik çalışanları, hibe yazarları ve proje yöneticileri arıyoruz.', 'team.open.btn': 'Açık Rolleri Görüntüle',

  /* CONTACT PAGE */
  'contact.label': 'İletişim', 'contact.title': 'Bize ulaşın.', 'contact.sub': 'Bir proje fikriniz mi var? Ortak olmak mı istiyorsunuz? Ya da sadece merhaba demek mi? Bize bir mesaj bırakın, 48 saat içinde size dönelim.',
  'contact.office': 'Ofisler', 'contact.off1': 'Berlin, Almanya', 'contact.off2': 'İstanbul, Türkiye',
  'contact.form.name': 'Adınız', 'contact.form.email': 'E-posta Adresi', 'contact.form.subject': 'Konu', 'contact.form.msg': 'Mesajınız', 'contact.form.send': 'Mesajı Gönder',
  'contact.form.success': 'Mesaj başarıyla gönderildi! Size en kısa sürede dönüş yapacağız.',

  /* VOLUNTEER PAGE */
  'vol.label': 'Gönüllü Ol', 'vol.title': 'Ekosistemi şekillendir.', 'vol.sub': 'Sadece zamanınızı istemiyoruz. Fikirlerinizi istiyoruz. 5 ülkeden 120+ genç değişimciden oluşan ağımıza katılın ve gençlik çalışmalarının geleceğini inşa etmemize yardımcı olun.',
  'vol.w1.title': 'Projelere Liderlik Et', 'vol.w1.desc': 'Sadece yardım etme. Yerel girişimlerin ve uluslararası gençlik değişimlerinin sahipliğini al.',
  'vol.w2.title': 'Ağını Kur', 'vol.w2.desc': 'Avrupa çapında STK\'lar, aktivistler ve girişimcilerle bağlantı kur.',
  'vol.w3.title': 'Yaparak Öğren', 'vol.w3.desc': 'Proje yönetimi, hibe yazımı ve etkinlik prodüksiyonunda uygulamalı deneyim kazan.',
  'vol.form.title': 'Gönüllü Başvurusu',
  'vol.form.area': 'İlgi Alanı', 'vol.form.a1': 'Etkinlik Organizasyonu', 'vol.form.a2': 'İçerik & Medya', 'vol.form.a3': 'Proje Yazımı (Erasmus+)', 'vol.form.a4': 'Araştırma & Veri',
  'vol.form.mot': 'Neden YouthTICK\'e katılmak istiyorsun?', 'vol.form.submit': 'Başvuruyu Gönder'
};

const de = {
  /* NAV */
  'nav.home': 'Startseite', 'nav.about': 'Über uns', 'nav.focus': 'Schwerpunkte',
  'nav.projects': 'Projekte', 'nav.partnership': 'Partnerschaften',
  'nav.impact': 'Wirkung', 'nav.blog': 'Einblicke', 'nav.team': 'Team',
  'nav.contact': 'Kontakt', 'nav.join': 'Mitmachen',

  /* HERO */
  'hero.badge': 'Europäisches Jugendnetzwerk · Gegr. 2026',
  'hero.title1': 'Jugend,', 'hero.title2': 'Kultur',
  'hero.title3': 'und Handeln', 'hero.title4': 'verbinden.',
  'hero.sub': 'YouthTICK ist ein zeitgemäßes Jugendnetzwerk, das junge Menschen durch internationale Zusammenarbeit, Innovation und kulturellen Austausch stärkt.',
  'hero.cta1': 'Projekte entdecken', 'hero.cta2': 'Freiwilliger werden', 'hero.cta3': 'Partner werden',
  'hero.trust': 'Aktiv in 5 Ländern · 120+ Teilnehmende',
  'hero.badge1.num': '5', 'hero.badge1.label': 'Länder',
  'hero.badge2.num': 'Erasmus+', 'hero.badge2.label': 'Partner',

  /* TRUST BAR */
  'trust.label': 'Unterstützt von & kooperiert mit',

  /* ABOUT TEASER (Home) */
  'about.label': 'Wer wir sind', 'about.title': 'Eine neue Art von Jugendorganisation.',
  'about.p1': 'YouthTICK arbeitet an der Schnittstelle von internationaler Mobilität, zivilgesellschaftlicher Teilhabe und unternehmerischem Denken.',
  'about.p2': 'Von Berlin bis Istanbul, von Erasmus+-Austauschen bis hin zu Innovationslaboren – wir bauen Ökosysteme, die Ambitionen in Handlungen umwandeln.',
  'about.cta': 'Unsere Geschichte',

  /* STATS (Home & Impact) */
  'stat1.label': 'Laufende Projekte (2026)', 'stat2.label': 'Jugendliche Teilnehmende',
  'stat3.label': 'Aktive Länder', 'stat4.label': 'Partnerorganisationen',

  /* FOCUS (Home & Focus Page) */
  'focus.label': 'Was wir tun', 'focus.title': 'Sechs Säulen der Jugendarbeit.',
  'focus.all': 'Alle Bereiche →',
  'focus.f1.title': 'Erasmus+ Projekte', 'focus.f1.desc': 'Jugendaustausche, Trainingskurse und strategische Partnerschaften in Europa.',
  'focus.f2.title': 'Jugendbeteiligung', 'focus.f2.desc': 'Zivilgesellschaftliches Engagement, demokratische Prozesse und Bürgerprogramme.',
  'focus.f3.title': 'Unternehmertum', 'focus.f3.desc': 'Innovationslabore, Startup-Mentoring und Social-Entrepreneurship-Programme.',
  'focus.f4.title': 'Kultureller Austausch', 'focus.f4.desc': 'Interkultureller Dialog, Kunst, Erbe und kreative Austauschprogramme.',
  'focus.f5.title': 'Forschung & Berichte', 'focus.f5.desc': 'Datengestützte Jugendforschung, Politikpapiere und Wirkungsmessung.',
  'focus.f6.title': 'Internationales Netzwerk', 'focus.f6.desc': 'Grenzüberschreitende Partnerschaften, NGO-Koalitionen und globale Jugendforen.',

  /* PROJECTS */
  'proj.label': 'Aktuelle Arbeit', 'proj.title': 'Ausgewählte Projekte.', 'proj.all': 'Alle Projekte →',
  'proj.page.title': 'Projekte & Initiativen', 'proj.page.sub': 'Von lokalen Innovationen bis zu europäischen Netzwerken. Hier ist, was wir aufbauen.',
  'proj.active': 'Laufende Projekte', 'proj.past': 'Vergangene Projekte',

  /* PULLQUOTE */
  'quote.text': 'YouthTICK hat mir eine Plattform gegeben, die ich nicht wusste, dass ich sie brauche — um zu vernetzen, aufzubauen und zu führen.',
  'quote.author': 'Mia Schneider', 'quote.role': 'Jugendaustausch-Teilnehmerin · Berlin, Deutschland',

  /* BLOG */
  'blog.label': 'Einblicke', 'blog.title': 'Geschichten, Forschung und Updates aus dem Netzwerk.',
  'blog.all': 'Alle Artikel →',

  /* CTA BANNER */
  'cta.title': 'Bereit, Teil von etwas Größerem zu sein?',
  'cta.sub': 'Tritt einem Netzwerk von 120+ jungen Changemakers aus 5 Ländern bei.',
  'cta.btn1': 'Als Freiwilliger beitreten', 'cta.btn2': 'Kontakt aufnehmen',

  /* FOOTER */
  'footer.tagline': 'Ein zeitgemäßes europäisches Jugendnetzwerk, das junge Menschen durch internationale Zusammenarbeit, Innovation und kulturellen Austausch stärkt.',
  'footer.copy': '© 2026 YouthTICK. Alle Rechte vorbehalten.',
  'footer.connect': 'Kontakt', 'footer.community': 'Gemeinschaft', 'footer.platform': 'Plattform',

  /* ABOUT PAGE */
  'about.page.title': 'Über YouthTICK',
  'about.mission.title': 'Mission', 'about.mission.text': 'Junge Menschen mit Werkzeugen, Netzwerken und Möglichkeiten auszustatten, um ihre eigene Zukunft zu gestalten und einen sinnvollen Beitrag zur europäischen Gesellschaft zu leisten.',
  'about.vision.title': 'Vision', 'about.vision.text': 'Ein Europa, in dem jeder junge Mensch – unabhängig von seiner Herkunft – eine gleichberechtigte Stimme, gleiche Chancen und die gleiche Handlungsfähigkeit hat, um Veränderungen herbeizuführen.',
  'about.lead': '"Wir machen keine Programme für Jugendliche. Wir bauen Infrastruktur mit Jugendlichen."',
  'about.m1': 'YouthTICK entstand aus einer einfachen, aber radikalen Überzeugung: Junge Menschen sind nicht die Führungskräfte von morgen – sie sind die Führungskräfte von heute. Wir existieren, um diese Überzeugung nicht nur rhetorisch, sondern operativ umzusetzen.',
  'about.m2': 'Gegründet im Jahr 2026 an der Schnittstelle des kreativen Ökosystems Berlins und der unternehmerischen Energie Istanbuls, ist YouthTICK ein Jugendnetzwerk der neuen Generation, das in 5 Ländern aufgebaut wird. Wir gestalten Erlebnisse – Austausche, Labs, Foren, Trainingskurse – die sich um die tatsächlichen Ambitionen junger Menschen drehen, nicht um institutionelle Agenden.',
  'about.m3': 'Unsere Arbeit umfasst Erasmus+ Projektmanagement, politische Bildung, kulturelle Programme und soziales Unternehmertum. Was alles verbindet, ist das Engagement für eine sinnvolle Beteiligung – keine bloße Alibi-Inklusion, sondern echte Mitgestaltung.',
  'about.m4': 'Wir bauen aktiv unsere Erasmus+ Anerkennung und Partnerschaftsnetzwerke auf. Wir arbeiten mit SALTO, JUGEND für Europa und dem Europäischen Jugendforum zusammen. Am stolzesten sind wir auf die 120+ jungen Menschen, die sich bereits in unseren Programmen 2026 engagieren, und auf die Pipeline ehrgeiziger Projekte, die vor uns liegen.',
  
  'about.values.label': 'Wofür wir stehen', 'about.values.title': 'Sechs Werte, die alles antreiben, was wir tun.',
  'about.v1.title': 'Handlungsfähigkeit vor Teilnahme', 'about.v1.desc': 'Wir entwerfen für Entscheidungsmacht, nicht nur für Inklusion. Junge Menschen gestalten unsere Programme, sie besuchen sie nicht nur.',
  'about.v2.title': 'Offenheit als Infrastruktur', 'about.v2.desc': 'Alle unsere Methoden, Toolkits und Berichte sind standardmäßig Open-Source. Wissen sollte sich vermehren, nicht gehortet werden.',
  'about.v3.title': 'Wirkung vor Optik', 'about.v3.desc': 'Wir messen Ergebnisse, keine bloßen Outputs. Die Tiefe der Transformation schlägt in allem, was wir tun, die Breite der Reichweite.',
  'about.v4.title': 'Kulturelle Demut', 'about.v4.desc': 'Wir arbeiten über mehrere Kulturen hinweg und wissen, dass kein einziges Modell für alle passt. Wir passen uns an, hören zu und iterieren ständig.',
  'about.v5.title': 'Radikale Zusammenarbeit', 'about.v5.desc': 'Die komplexesten Herausforderungen der Jugend erfordern NGOs, Regierungen, Startups und Universitäten am selben Tisch.',
  'about.v6.title': 'Nachhaltigkeit im Kern', 'about.v6.desc': 'Ökologische, soziale und institutionelle Nachhaltigkeit ist kein bloßer Schwerpunkt – es ist eine Perspektive, die wir auf alles anwenden, was wir tun.',

  'about.journey.label': 'Unsere Reise', 'about.journey.title': 'Unsere Reise — von der Idee zum Netzwerk.',
  'about.j1.date': 'Q1 2026', 'about.j1.text': 'YouthTICK in Berlin gegründet. Kernteam aus Deutschland und der Türkei zusammengestellt. Erste Partnerschaftsverträge unterzeichnet.',
  'about.j2.date': 'Q2 2026', 'about.j2.text': 'Erster Jugendaustausch zwischen Deutschland und der Türkei gestartet. 40 Teilnehmer. Erasmus+ Antrag eingereicht.',
  'about.j3.date': 'Q3 2026', 'about.j3.text': 'Zweites Projekt gestartet. Innovationslabor-Pilotprogramm beginnt in Berlin. 80+ Jugendliche erreicht.',
  'about.j4.date': 'H2 2026 — Geplant', 'about.j4.text': '3+ aktive Projekte, 5 Länder, 120+ Teilnehmer. Erster Jahresbericht wird veröffentlicht. Erasmus+ Akkreditierung in Arbeit.',

  /* IMPACT PAGE */
  'impact.label': 'Unsere Wirkung', 'impact.title': 'Eine neue Generation messbarer Veränderungen.', 'impact.sub': 'Jede Zahl repräsentiert eine echte Person, ein echtes Projekt, eine echte Transformation. Hier sind die Fakten.',
  'impact.yy.label': 'Jahr für Jahr', 'impact.yy.title': 'Wachstum in jeder Dimension.',
  'impact.yy.launch': 'Gestartetes Projekt', 'impact.yy.part': 'Teilnehmende', 'impact.yy.country': 'Länder', 'impact.yy.active': 'Aktive Projekte', 'impact.yy.proj': 'Projekte',
  
  'impact.sdg.title': 'Beitrag zu globalen Zielen.',
  'impact.sdg1': 'SDG 4 — Hochwertige Bildung', 'impact.sdg1.desc': 'Nicht formales Lernen, Kompetenzentwicklung und Zugang zu lebenslangem Lernen für alle jungen Menschen.',
  'impact.sdg2': 'SDG 10 — Weniger Ungleichheiten', 'impact.sdg2.desc': 'Schaffung von Chancengleichheit für Jugendliche unabhängig vom geografischen oder sozioökonomischen Hintergrund.',
  'impact.sdg3': 'SDG 13 — Maßnahmen zum Klimaschutz', 'impact.sdg3.desc': 'Aufbau der nächsten Generation von Umweltaktivisten und Nachhaltigkeitspraktikern.',
  'impact.sdg4': 'SDG 17 — Partnerschaften', 'impact.sdg4.desc': 'Transnationale Zusammenarbeit als Eckpfeiler jedes Programms, das wir entwerfen und durchführen.',
  'impact.sdg5': 'SDG 11 — Nachhaltige Städte', 'impact.sdg5.desc': 'Von Jugendlichen geleitete urbane Innovationsprogramme, die lebenswertere, integrative Städte in ganz Europa gestalten.',
  'impact.sdg6': 'SDG 16 — Frieden & Institutionen', 'impact.sdg6.desc': 'Politische Bildung, demokratische Partizipation und interkultureller Dialog als Grundlagen des Friedens.',
  'impact.sdg7': 'SDG 8 — Menschenwürdige Arbeit', 'impact.sdg7.desc': 'Jugendunternehmertumsprogramme, die nachhaltige wirtschaftliche Wege für junge Menschen schaffen.',
  'impact.sdg8': 'SDG 5 — Geschlechtergleichheit', 'impact.sdg8.desc': 'Alle Programme werden mit der Geschlechtergleichstellung als Kernprinzip entwickelt, nicht als nachträglicher Gedanke.',

  'impact.rep.title': 'Unsere Forschung, frei verfügbar.',
  'impact.rep1.date': '2026 — Demnächst', 'impact.rep1.title': 'YouthTICK Gründungsbericht: Jugendbeteiligung in Südosteuropa 2026', 'impact.rep1.meta': 'Erwartet: Q4 2026 · Verfügbar in EN, TR, DE',
  'impact.rep2.date': '2026 — In Arbeit', 'impact.rep2.title': 'Deutsch-Türkische Jugendmobilität: Landschaft & Chancen', 'impact.rep2.meta': 'Entwurf · Mitverfasst mit JUGEND für Europa · Erwartet Q3 2026',
  'impact.rep.notify': 'Benachrichtigen', 'impact.rep.collab': 'Zusammenarbeiten →',

  /* PARTNERSHIPS PAGE */
  'part.title': 'Bauen Sie mit uns.', 'part.sub': 'Die komplexesten Herausforderungen der Jugend erfordern radikale Zusammenarbeit. Wir arbeiten mit NGOs, Universitäten, Kommunen und fortschrittlichen Unternehmen zusammen, um skalierbare Wirkung zu erzielen.',
  'part.net.label': 'Unser Netzwerk', 'part.net.title': 'Globale Reichweite, lokale Wurzeln.',
  'part.join.label': 'Partner werden', 'part.join.title': 'Lassen Sie uns die nächste Generation von Jugendprogrammen aufbauen.',
  'part.join.sub': 'Ob Sie eine NGO sind, die einen zuverlässigen Erasmus+-Partner sucht, oder eine Kommune, die Jugendliche einbinden möchte – wir bringen das Fachwissen, das Netzwerk und die Energie mit, um dies zu verwirklichen.',
  'part.t1': 'Erasmus+ Konsortium', 'part.t1.desc': 'Suchen Sie einen zuverlässigen Partner in Deutschland oder der Türkei? Wir sind auf KA1-Mobilität und KA2-strategische Partnerschaften spezialisiert.',
  'part.t2': 'Forschung & Daten', 'part.t2.desc': 'Wir arbeiten mit Universitäten und Think Tanks zusammen, um Feldforschung zu Jugendtrends und -politik durchzuführen.',
  'part.t3': 'Corporate CSR', 'part.t3.desc': 'Richten Sie Ihre Ziele zur sozialen Verantwortung auf hochwirksame Programme für Jugendunternehmertum und Nachhaltigkeit aus.',
  'part.t4': 'Lokale Umsetzung', 'part.t4.desc': 'Wir helfen Kommunen und lokalen Regierungen, jugendfreundliche Politiken und partizipative Räume zu gestalten.',
  'part.cta.title': 'Bereit zur Zusammenarbeit? Lassen Sie uns sprechen.',

  /* TEAM PAGE */
  'team.label': 'Unser Team', 'team.title': 'Die Menschen hinter dem Netzwerk.', 'team.sub': 'Eine vielfältige Gruppe von Jugendarbeitern, Forschern, Designern und Strategen, die europaweit arbeiten, um die nächste Generation zu stärken.',
  'team.r1': 'Mitbegründer & Direktor', 'team.r2': 'Leiterin der Programme (DE)', 'team.r3': 'Erasmus+ Koordinator', 'team.r4': 'Community Manager',
  'team.r5': 'Forschungsleiter', 'team.r6': 'Kreativdirektor', 'team.r7': 'Partnerschaften (TR)', 'team.r8': 'Jugendvertreter',
  'team.open.title': 'Schließe dich dem Kernteam an', 'team.open.desc': 'Wir sind immer auf der Suche nach leidenschaftlichen Jugendarbeitern, Grant-Writern und Projektmanagern, die sich unserem wachsenden Netzwerk anschließen.', 'team.open.btn': 'Offene Rollen anzeigen',

  /* CONTACT PAGE */
  'contact.label': 'Kontakt', 'contact.title': 'Nehmen Sie Kontakt auf.', 'contact.sub': 'Haben Sie eine Projektidee? Möchten Sie eine Partnerschaft eingehen? Oder einfach nur Hallo sagen? Hinterlassen Sie uns eine Nachricht und wir melden uns innerhalb von 48 Stunden bei Ihnen.',
  'contact.office': 'Büros', 'contact.off1': 'Berlin, Deutschland', 'contact.off2': 'Istanbul, Türkei',
  'contact.form.name': 'Ihr Name', 'contact.form.email': 'E-Mail-Adresse', 'contact.form.subject': 'Betreff', 'contact.form.msg': 'Ihre Nachricht', 'contact.form.send': 'Nachricht Senden',
  'contact.form.success': 'Nachricht erfolgreich gesendet! Wir werden uns in Kürze bei Ihnen melden.',

  /* VOLUNTEER PAGE */
  'vol.label': 'Freiwillige', 'vol.title': 'Gestalte das Ökosystem.', 'vol.sub': 'Wir wollen nicht nur Ihre Zeit. Wir wollen Ihre Ideen. Schließen Sie sich unserem Netzwerk von 120+ jungen Changemakers an und helfen Sie uns, die Zukunft der Jugendarbeit aufzubauen.',
  'vol.w1.title': 'Projekte leiten', 'vol.w1.desc': 'Assistieren Sie nicht nur. Übernehmen Sie die Verantwortung für lokale Initiativen und internationale Jugendaustausche.',
  'vol.w2.title': 'Netzwerk aufbauen', 'vol.w2.desc': 'Vernetzen Sie sich mit NGOs, Aktivisten und Unternehmern in ganz Europa.',
  'vol.w3.title': 'Lernen durch Tun', 'vol.w3.desc': 'Sammeln Sie praktische Erfahrungen im Projektmanagement, beim Schreiben von Anträgen und in der Veranstaltungsproduktion.',
  'vol.form.title': 'Freiwilligenbewerbung',
  'vol.form.area': 'Interessengebiet', 'vol.form.a1': 'Eventorganisation', 'vol.form.a2': 'Inhalt & Medien', 'vol.form.a3': 'Projektschreiben (Erasmus+)', 'vol.form.a4': 'Forschung & Daten',
  'vol.form.mot': 'Warum möchtest du YouthTICK beitreten?', 'vol.form.submit': 'Bewerbung einreichen'
};

const TRANSLATIONS = { en, tr, de };

const i18nOutput = `const TRANSLATIONS = ${JSON.stringify(TRANSLATIONS, null, 2)};

/* ── Language state ─────────────────────────────────────────── */
let currentLang = 'en';

try {
  currentLang = localStorage.getItem('yt_lang') || 'en';
} catch (e) {}

function setLanguage(lang) {
  if (!TRANSLATIONS[lang]) return;
  currentLang = lang;
  
  try {
    localStorage.setItem('yt_lang', lang);
  } catch(e) {}

  /* Update all data-i18n elements */
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    const val = TRANSLATIONS[lang][key];
    if (val !== undefined) {
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = val;
      } else {
        el.innerHTML = val; // using innerHTML to support <br> etc if needed, though textContent is safer. Wait, some have HTML like <em>.
      }
    }
  });

  /* Special case: Document Title */
  const titleKey = document.title.includes('YouthTICK') ? document.body.dataset.titleKey : null;
  if(titleKey && TRANSLATIONS[lang][titleKey]) {
     document.title = TRANSLATIONS[lang][titleKey] + ' — YouthTICK';
  }

  /* Update HTML lang attribute */
  document.documentElement.lang = lang;

  /* Update all lang buttons */
  document.querySelectorAll('.lang-btn, .mobile-lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
}

function t(key) {
  return (TRANSLATIONS[currentLang] && TRANSLATIONS[currentLang][key]) || (TRANSLATIONS.en && TRANSLATIONS.en[key]) || key;
}

// Run immediately to prevent FOUT if DOM is already parsed
setLanguage(currentLang);

// Also run on DOMContentLoaded to catch elements generated later or elements in the body if this script is in head
document.addEventListener('DOMContentLoaded', () => {
  setLanguage(currentLang);
});
`;

fs.writeFileSync('i18n.js', i18nOutput);
console.log("i18n.js written successfully.");
