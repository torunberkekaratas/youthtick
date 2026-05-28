# 🗺️ Yalova Keyword Cluster Map — Visual Overview

## Cluster Architecture Diagram

```mermaid
graph TB
    subgraph PILLAR["🏛️ PILLAR PAGE"]
        P[yalova-genclik.html<br/>2500-3000 words<br/>✅ EXISTS]
    end
    
    subgraph C1["📚 CLUSTER 1: Erasmus & International"]
        S1A[yalova-erasmus.html<br/>1800 words<br/>✅ EXISTS<br/>HIGH PRIORITY]
        S1B[yalova-esc-gonullu.html<br/>1500 words<br/>🆕 NEW<br/>HIGH PRIORITY]
    end
    
    subgraph C2["👥 CLUSTER 2: Community & Projects"]
        S2A[yalova-genclik-toplulugu.html<br/>1200 words<br/>✅ EXISTS<br/>HIGH PRIORITY]
        S2B[yalova-genclik-projeleri.html<br/>1400 words<br/>🆕 NEW<br/>MEDIUM PRIORITY]
    end
    
    subgraph C3["🎓 CLUSTER 3: University & Students"]
        S3A[yalova-universite.html<br/>1600 words<br/>✅ EXISTS<br/>HIGH PRIORITY]
        S3B[yalova-ogrenci-firsatlari.html<br/>1300 words<br/>🆕 NEW<br/>MEDIUM PRIORITY]
    end
    
    subgraph C4["🗣️ CLUSTER 4: Language & Skills"]
        S4A[yalova-dil-okulu.html<br/>1400 words<br/>🆕 NEW<br/>HIGH PRIORITY]
        S4B[yalova-genclik-egitimi.html<br/>1300 words<br/>🆕 NEW<br/>MEDIUM PRIORITY]
    end
    
    subgraph C5["🏢 CLUSTER 5: Organizations"]
        S5A[yalova-genclik-orgutleri.html<br/>1100 words<br/>🆕 NEW<br/>LOW PRIORITY]
    end
    
    %% Pillar to Spokes (Mandatory Links)
    P --> S1A
    P --> S1B
    P --> S2A
    P --> S2B
    P --> S3A
    P --> S3B
    P --> S4A
    P --> S4B
    P --> S5A
    
    %% Spokes back to Pillar (Mandatory)
    S1A --> P
    S1B --> P
    S2A --> P
    S2B --> P
    S3A --> P
    S3B --> P
    S4A --> P
    S4B --> P
    S5A --> P
    
    %% Within Cluster Links
    S1A <--> S1B
    S2A <--> S2B
    S3A <--> S3B
    S4A <--> S4B
    
    %% Cross-Cluster Strategic Links
    S1A -.-> S4A
    S1A -.-> S2A
    S1A -.-> S3A
    S4A -.-> S3A
    S1B -.-> S2B
    S3B -.-> S1B
    
    classDef pillarStyle fill:#6366f1,stroke:#4f46e5,stroke-width:3px,color:#fff
    classDef existsStyle fill:#22c55e,stroke:#16a34a,stroke-width:2px,color:#fff
    classDef newHighStyle fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#fff
    classDef newMedStyle fill:#3b82f6,stroke:#2563eb,stroke-width:2px,color:#fff
    classDef newLowStyle fill:#94a3b8,stroke:#64748b,stroke-width:2px,color:#fff
    
    class P pillarStyle
    class S1A,S2A,S3A existsStyle
    class S1B,S4A newHighStyle
    class S2B,S3B,S4B newMedStyle
    class S5A newLowStyle
```

## Legend

### Page Status
- ✅ **EXISTS** = Already created, needs optimization
- 🆕 **NEW** = Needs to be created

### Priority Levels
- 🔴 **HIGH PRIORITY** = Create in Phase 2 (Week 3-4)
- 🟡 **MEDIUM PRIORITY** = Create in Phase 3 (Week 5-6)
- 🔵 **LOW PRIORITY** = Create in Phase 4 (Week 7-8)

### Link Types
- **Solid arrows (→)** = Mandatory links (pillar ↔ spokes)
- **Double arrows (↔)** = Bidirectional links within cluster
- **Dotted arrows (-.->)** = Optional cross-cluster links

---

## Quick Reference: Content Status

| Page | Status | Word Count | Priority | Phase |
|------|--------|------------|----------|-------|
| yalova-genclik.html | ✅ Exists | 2500 (expand) | Critical | 1 |
| yalova-erasmus.html | ✅ Exists | 1800 (optimize) | High | 1 |
| yalova-genclik-toplulugu.html | ✅ Exists | 1200 (optimize) | High | 1 |
| yalova-universite.html | ✅ Exists | 1600 (optimize) | High | 1 |
| **yalova-esc-gonullu.html** | 🆕 New | 1500 | High | 2 |
| **yalova-dil-okulu.html** | 🆕 New | 1400 | High | 2 |
| **yalova-genclik-projeleri.html** | 🆕 New | 1400 | Medium | 3 |
| **yalova-ogrenci-firsatlari.html** | 🆕 New | 1300 | Medium | 3 |
| **yalova-genclik-egitimi.html** | 🆕 New | 1300 | Medium | 3 |
| **yalova-genclik-orgutleri.html** | 🆕 New | 1100 | Low | 4 |

---

## Implementation Priority Matrix

```
┌─────────────────────────────────────────────────┐
│  CRITICAL (Do First)                            │
│  └─ yalova-genclik.html (Expand Pillar)        │
└─────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────┐
│  HIGH PRIORITY (Phase 1-2)                      │
│  ├─ yalova-erasmus.html (Optimize)             │
│  ├─ yalova-genclik-toplulugu.html (Optimize)   │
│  ├─ yalova-universite.html (Optimize)          │
│  ├─ yalova-esc-gonullu.html (Create)           │
│  └─ yalova-dil-okulu.html (Create)             │
└─────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────┐
│  MEDIUM PRIORITY (Phase 3)                      │
│  ├─ yalova-genclik-projeleri.html (Create)     │
│  ├─ yalova-ogrenci-firsatlari.html (Create)    │
│  └─ yalova-genclik-egitimi.html (Create)       │
└─────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────┐
│  LOW PRIORITY (Phase 4)                         │
│  └─ yalova-genclik-orgutleri.html (Create)     │
└─────────────────────────────────────────────────┘
```

---

## SERP Overlap Heatmap (Simulated)

```
                ┌──────────────────────────────────────────┐
                │  Overlap Intensity                       │
                │  🟥 9-10 = Same Post                     │
                │  🟧 7-8  = Same Post                     │
                │  🟨 4-6  = Same Cluster                  │
                │  🟩 2-3  = Interlink                     │
                │  ⬜ 0-1  = Separate                      │
                └──────────────────────────────────────────┘

                     e   e   g   g   ü   d   t
                     r   s   e   e   n   i   3
                     a   c   n   n   i   l
                     s       ç   ç   v
                     m       l   l   e
                     u       i   i   r
                     s       k   k   s
                             .   .   i
                                 t   t
                                 o   e
                                 p   s
                                 l   i
                                 .

erasmus           🟥  🟨  🟨  🟨  🟩  🟨  🟩
esc               🟨  🟥  🟨  🟨  🟩  🟩  🟩
gençlik           🟨  🟨  🟥  🟧  🟩  🟩  🟩
gençlik.topl.     🟨  🟨  🟧  🟥  🟩  ⬜  🟨
üniversitesi      🟩  🟩  🟩  🟩  🟥  🟩  ⬜
dil okulu         🟨  🟩  🟩  ⬜  🟩  🟥  ⬜
t3                🟩  🟩  🟩  🟨  ⬜  ⬜  🟥
```

---

## Traffic Flow Projection (6 Months)

```
                    PILLAR PAGE
               yalova-genclik.html
                 📊 1200 visits/mo
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   [CLUSTER 1]    [CLUSTER 2]     [CLUSTER 3]
   Erasmus 🌍     Community 👥    University 🎓
   600 v/mo       400 v/mo        500 v/mo
        │               │               │
    ┌───┴───┐       ┌───┴───┐       ┌───┴───┐
    │       │       │       │       │       │
   S1A    S1B     S2A     S2B     S3A     S3B
   400v   200v    250v    150v    300v    200v
   
        │               │
   [CLUSTER 4]    [CLUSTER 5]
   Language 🗣️    Orgs 🏢
   350 v/mo       150 v/mo
        │               │
    ┌───┴───┐           │
    │       │           │
   S4A    S4B         S5A
   200v   150v        150v

────────────────────────────────────────────
TOTAL: ~3,850 visits/month (projected)
```

---

## Internal Link Density Map

```
Pages by Incoming Link Count (Target)

yalova-genclik.html          ████████████████████ 20+ links
yalova-erasmus.html          ████████████ 12 links
yalova-genclik-toplulugu.html ███████████ 11 links
yalova-universite.html       ██████████ 10 links
yalova-dil-okulu.html        █████████ 9 links
yalova-esc-gonullu.html      ████████ 8 links
yalova-genclik-projeleri.html ███████ 7 links
yalova-ogrenci-firsatlari.html ██████ 6 links
yalova-genclik-egitimi.html  ██████ 6 links
yalova-genclik-orgutleri.html ████ 4 links
```

---

## Next Actions Checklist

### Week 1-2 (Phase 1: Optimize Existing)
- [ ] Expand `yalova-genclik.html` to 2500+ words
- [ ] Add internal links from pillar to all existing spokes
- [ ] Add "back to pillar" links from all spokes
- [ ] Optimize meta titles and descriptions
- [ ] Add FAQ sections to existing pages
- [ ] Test internal linking structure

### Week 3-4 (Phase 2: High Priority New Pages)
- [ ] Create `yalova-esc-gonullu.html` (1500 words)
- [ ] Create `yalova-dil-okulu.html` (1400 words)
- [ ] Link new pages to pillar (bidirectional)
- [ ] Add within-cluster links
- [ ] Add cross-cluster strategic links
- [ ] Update sitemap.xml

### Week 5-6 (Phase 3: Medium Priority)
- [ ] Create `yalova-genclik-projeleri.html` (1400 words)
- [ ] Create `yalova-ogrenci-firsatlari.html` (1300 words)
- [ ] Create `yalova-genclik-egitimi.html` (1300 words)
- [ ] Complete all internal linking
- [ ] Add schema markup to all pages

### Week 7-8 (Phase 4: Finalize)
- [ ] Create `yalova-genclik-orgutleri.html` (1100 words)
- [ ] Final internal linking audit
- [ ] Test all links
- [ ] Submit updated sitemap to Google Search Console
- [ ] Monitor rankings

---

**Total Pages:** 10 (4 existing + 6 new)  
**Total Word Count:** ~15,900 words  
**Implementation Timeline:** 8 weeks  
**Expected Traffic Increase:** +300-400% in 6 months

---

**Files Generated:**
1. `/cluster-analysis-yalova.md` — Detailed analysis
2. `/cluster-plan-yalova.json` — Structured data
3. `/cluster-map-yalova.md` — This visual overview

**Last Updated:** May 28, 2026
