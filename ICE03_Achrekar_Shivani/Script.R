install.packages("stringr")
install.packages("tidyverse")


a = c('Cathrin', 'Cathryn', 'Cathrinn', 'Cathrynn', 'Cathrine', 'Cathryne', 'Cathrinne',
    'Cathrynne')
'Catherinne', 'Catherynne')
grep("Cather[i{1}y{1}](n|nn|ne|nne)", b, value = TRUE)
'Kathrynne')
grep("Kathr[i{1}y{1}](n|nn|ne|nne)", c, value = TRUE)
grep("Kathr(i|y)(n|nn)|(ne|nne)", c, value = TRUE)
grep("Kathr(i|y)(n{1}|nn{1}|ne{1}|nne{1})", c, value = TRUE)
grep("Kathr[i{1}y{1}](n|nn)|(ne|nne)", c, value = TRUE)


d = c('Katherin', 'Katheryn', 'Katherinn', 'Katherynn', 'Kattherine', 'Katheryne',
'Katherinne', 'Katherynne')
grep("Kat(t|)her[i{1}y{1}](n|nn|ne|nne)", d, value = TRUE)
grep("Kat(t|)her(i|y)(n|nn|ne|nne)", d, value = TRUE)
grep("Kat(t|)her(i|y)(n{1}|nn{1}|ne{1}|nne{1})", d, value = TRUE)
grep("Kat(t|)her(i{1}|y{1})(n|nn)(|ne|nne)", d, value = TRUE)


e = c('Catherin', 'Catheryn', 'Catherinn', 'Catherynn', 'Catherine', 'Catheryne',
'Catherinne', 'Catherynne','Catherin', 'Catheryn', 'Catherinn', 'Catherynn', 'Catherine', 'Catheryne',
'Catherinne', 'Catherynne', 'Kathrin', 'Kathryn', 'Kathrinn', 'Kathrynn', 'Kathrine', 'Kathryne', 'Kathrinne',
'Kathrynne', 'Katherin', 'Katheryn', 'Katherinn', 'Katherynn', 'Kattherine', 'Katheryne',
'Katherinne', 'Katherynne')
grep("[CK]at(t|)h(e|)r[iy](n|nn|ne|nne)", e, value = TRUE)

sentences

adverb = "\\b([^ ]+)ly"
adverb = "([A-Za-z]+ly)"
m = str_subset(sentences, adverb)
m
ma = str_extract(m, adverb)
ma

k = grep("\\b([^ ]+)ly [the]", m, value = TRUE)
k
j = grep("\\b([^ ]+)ly (a)", m, value = TRUE)
j


