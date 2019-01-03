import pandas as pd
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

#Parse the CSV
botspam          = pd.read_csv("csv/botspam.csv", error_bad_lines=False, sep=';', engine='python' )
general          = pd.read_csv("csv/general.csv", error_bad_lines=False, sep=';', engine='python' )
offtopic         = pd.read_csv("csv/offtopic.csv", error_bad_lines=False, sep=';', engine='python' )
spoilers         = pd.read_csv("csv/spoilers.csv", error_bad_lines=False, sep=';', engine='python' )
artworkandmusic  = pd.read_csv("csv/artworkandmusic.csv", error_bad_lines=False, sep=';', engine='python' )
newupcoming      = pd.read_csv("csv/newupcoming.csv", error_bad_lines=False, sep=';', engine='python' )
offtopicspoilers = pd.read_csv("csv/offtopicspoilers.csv", error_bad_lines=False, sep=';', engine='python' )
questions        = pd.read_csv("csv/questions.csv", error_bad_lines=False, sep=';', engine='python' )
redditwingsffxiv = pd.read_csv("csv/redditwingsffxiv.csv", error_bad_lines=False, sep=';', engine='python' )

#Take the top 25 users from each channel
authorsBotspam          = botspam.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsGeneral          = general.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsofftopic         = offtopic.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsspoilers         = spoilers.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsartworkandmusic  = artworkandmusic.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsnewupcoming      = newupcoming.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsofftopicspoilers = offtopicspoilers.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsquestions        = questions.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)
authorsredditwingsffxiv = redditwingsffxiv.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(25)


#Convine all dataframes into a single master dataframe
frames = [botspam,general,offtopic,spoilers,artworkandmusic,newupcoming,offtopicspoilers,questions,redditwingsffxiv]
csv = pd.concat(frames)
rows = csv.shape[0]
#And then the top 25 of the master dataframe
authors = csv.groupby('Author').Author.count().reset_index(name='count').sort_values(['count'], ascending=False).head(30)

#MESSAGE GRAPH

##botspam
plt.figure(figsize=(20,30))
authorsBotspam.plot.bar(tick_label="xd").set_xticklabels(authorsBotspam.Author)
plt.xlabel("Users - botspam")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/botspam.png')
##general
plt.figure(figsize=(20,30))
authorsGeneral.plot.bar(tick_label="xd").set_xticklabels(authorsGeneral.Author)
plt.xlabel("Users - general")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/general.png')
##offtopic
plt.figure(figsize=(20,30))
authorsofftopic.plot.bar(tick_label="xd").set_xticklabels(authorsofftopic.Author)
plt.xlabel("Users - offtopic")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/offtopic.png')
##spoilers
plt.figure(figsize=(20,30))
authorsspoilers.plot.bar(tick_label="xd").set_xticklabels(authorsspoilers.Author)
plt.xlabel("Users - spoilers")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/spoilers.png')
##artworkandmusic
plt.figure(figsize=(20,30))
authorsartworkandmusic.plot.bar(tick_label="xd").set_xticklabels(authorsartworkandmusic.Author)
plt.xlabel("Users - artworkandmusic")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/artworkandmusic.png')
##newupcoming
plt.figure(figsize=(20,30))
authorsnewupcoming.plot.bar(tick_label="xd").set_xticklabels(authorsnewupcoming.Author)
plt.xlabel("Users - newupcoming")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/newupcoming.png')
##offtopicspoilers
plt.figure(figsize=(20,30))
authorsofftopicspoilers.plot.bar(tick_label="xd").set_xticklabels(authorsofftopicspoilers.Author)
plt.xlabel("Users - offtopicspoilers")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/offtopicspoilers.png')
##questions
plt.figure(figsize=(20,30))
authorsquestions.plot.bar(tick_label="xd").set_xticklabels(authorsquestions.Author)
plt.xlabel("Users - questions")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/questions.png')
##redditwingsffxiv
plt.figure(figsize=(20,30))
authorsredditwingsffxiv.plot.bar(tick_label="xd").set_xticklabels(authorsredditwingsffxiv.Author)
plt.xlabel("Users - redditwingsffxiv")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/redditwingsffxiv.png')

##ALL THE CHANNELS
plt.figure(figsize=(20,30))
authors.plot.bar(tick_label="xd").set_xticklabels(authors.Author)
plt.xlabel("Users - ALL THE CHANNELS")
plt.ylabel("Number of Messages")
plt.tight_layout()
plt.savefig('graphs/all.png')

#WORDCLOUD GENERATOR


for user in authors.Author:
    text = ""
    print(user)
    userstr = str(user)
    authorSet = csv[ csv['Author'].str.contains(userstr) ] 
    for index, row in authorSet.iterrows():
        text += str(row['Content']).lower() + " "
    wordcloud = WordCloud(max_font_size=70,width=1000, height=1000, max_words=1000, background_color="black").generate(text)
    wordcloud.to_file('img/' + userstr + '.png')


