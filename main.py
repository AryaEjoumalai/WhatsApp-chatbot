#Execute the below block to untrain chatterbot
'''
from chatterbot import ChatBot
bot = ChatBot('Bot')
bot.storage.drop()
'''


#Uncomment the below block to train chatterbot with preset data
'''
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
'''


#Uncomment and modify the list in below block to custom train chatbot
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

t=['Apo field trip', 'Athu entha Saturday', 'Next  week..', 'Result yenna achu', '???', 'Therila..', 'Varala da', 'Okay', 'EM drawing measurement adula kudu Tu irukurada podanuma', 'Yup', 'Dae', 'Em  record la write pannanuma.?', 'Ela vena thoki potudu', 'Dae', 'Crt soldra', 'Venama??', 'Venam da', 'Ok..', 'Observation?', 'Nama acute angle fitting veraiku ezhudanuma', 'Ama da', 'Dae', 'Nalaiku dress code blue potu vanga da...', 'Lab dress potutu varalama', 'Venda nalla erukadhu..', 'Ena blue', 'Dark blue...', 'Erukuma??', 'Dei result vendhu cha', 'Vekala', 'Enna da', 'Naliku dress code colour??', 'Blue venam da', 'Vera sollu', 'Vera', 'White??', 'Blue Ella r kittauyum eruku da', 'I am not having da', 'Dark aa', 'Blue eruku la..', 'Mm..', 'Nee than leave aache', 'Varuvan da', 'Nee yenna colour solra', 'Blue kk va', 'Dae', 'Enna da blue ok va??', 'Enaku ok..', 'Black venama', 'Black la Ella da', 'Yaarkitayum..', 'Blue kk da', 'Dae', 'Ellarum dark blue potu vanga..', 'Bluetooth speakers', ',??????', "Noo.. bro it's  not  working...", 'Any others', 'Gm', 'Blue confirm ma', 'Ama..da', 'Ethana peru bule follow pannariga', 'Dress code', 'Nop', 'Enna dress. Code ra', 'Today', 'Filed trip iki da', "Today's special", 'Yep', 'Oh', 'Any photos available', '???', 'Photo aduthadhu Ella anapunga da', 'Aven penchatha yen bottle la full panniruke', '�', "Yesterday's notes send pannunga", '??', 'Enna notes', 'Ella subjects um enna notes koduthangalo adhu', 'Fan madw', 'Ama da', 'Nakku. Da', 'https', 'Real aa da', 'Therila', 'Nee panniya', 'Da', 'Fake da', 'Theriyum', 'Yellararoda number um kedailuma da', 'Purila..', 'Namma class yellaroda reg no venum da', 'Illa da entity..', '*enkitta..', 'Kk da', 'Vetla sollitiya', 'Da', 'Illa da', 'Sonna enaa  agum nu therila..', 'Naan sollitan da', 'Enna sonnanga?', 'Pathukalam nu sonnanga da', 'Mm..', 'MS ans send pannu ga da', 'Notes write panna laya??', 'Class irukuda', 'Dae', 'Open agamatikudhu..', 'Appo therila da', 'Enaku', 'Download WPS office', 'Bc Questions LA photo eaduthu send panuda', 'Book ka class LA vachita', 'Nandri bala', 'Yenn bala iruta iruku', 'Yenna panikitu iruka', 'Light poda la..�', '�', '�', 'Edhula enna da...', 'Nalla yenna ya kadala yenna ya', 'Da', 'Ohhh.. cringe ahh...', 'Bomboil', 'Dae', 'Adhu palm oil', 'Bomb oil theriyatha', '��', 'Palm oil ah?', 'Yes palmolien �', 'Hmm..', '�', 'https', 'Bhais assignment  sum anapunga......', 'Em..', 'Dae', 'Eruka illaya..???', 'Ila da', 'Re evaluation any one filled', 'Send pannunga da', 'Illa da', 'Adhukulley velaya aaramichitiya??', 'More than 45 min��', '2 marks ', '11 marks', 'Dei', 'Plzz', 'Akash del pannu..', 'Why', '��', '�', 'Delete pannuda enda ippadi panra', 'English unit 2 11 mark eruntha send panunga', 'Atha...ila da', '��', 'Ok', 'Unit 2 da', 'Ila da �', 'Chemistry 2nd assignment what?', 'Manual la eruka 2nd exp dha...', '� *Internship Opportunities*', 'What', 'Manual   erukura 2nd exp dha da...', 'Ok', 'Mm..', 'Ennadu da ithu', 'Internship da', 'Entha company', 'Ibm', 'Yaaru venalum join pannalama', 'Hmm', '*Only 5 slots are allocated for Manakula Vinayagar Institute of Technology*', 'For wat da', 'English test portion enna da??', 'Dae', 'Sollunga da', 'Naku', 'Dae', '11 marks', '2 marks ', 'Setha payalae...', 'Tq da palkova...', 'Dei', 'Nalaiku English exam ah', 'S', 'Kk. Da', 'Chemistry first assignment enathu', 'Mineral wealth  of India..', 'Ok', 'Maths qp anupunga. Da', 'Dae', 'S', 'Em assignment finish pana send panunga', 'Dae', 'Hmm bu da', '�', 'For me also', 'Poda ....', 'Any one completed em', 'No da', '��', 'Arya va kelungga da', 'Arya junction impact play panituerupa', 'Avan phone aa yedula matan da', 'Ama da', 'Arounesh kitta kelunga da', 'Adhu genshin da', 'Eathavathu mudicha send panunga da', '�\u200d♂️assignment mudchita pola', 'Em question paper send panunga', 'Yaaru thu da ithu', '???', 'Patha ealuthu da', 'Yaara', 'Remaining sums yaravathu pota send panunga', 'Crt ahh therila check panni paru...', 'Theriyama eathuku DA pota', 'Poturka check karoo..', 'Moment kandu pudi', 'Kandu pudichita...', 'Adu illa anda supportuku oru moment varum', 'Andha support?', 'Correct dan lasta sigma moment A nu podu', 'Ok da', 'Hey Ellarum note pannikonga..', 'Aduku equal to 0 varadu', 'Adhula..', 'Ok �', 'Dae endha ans crt note pannikonga..', 'Ok', 'No dude, il pick up!', 'I was really playing genshin impact and saw these messages jn', 'Apologies for any offense', '(Non existent offence)', 'Why?', "That's why non existent", 'Nee poi toongu nalaiku pesikalam', 'Not sleeping time', 'Seri poivplay pannu', 'Jaichitom maara', 'Good evening mam', 'Letter ezhudu', 'Nalli ku EM enna test', 'Retest...', 'Em assignment qns annapugada', 'Collage irukka ?', 'Iruku', 'Inaiku vantha qp ah da', '?', 'Aama', 'Nalaiku vara questions paper send pannu da arounesh', 'Ithu tha da', 'Athu', '..', '��', 'Mit cse la y podala da nee', 'Theva.  Ilq da', 'Ellarukumla..anupatha', '2 marks send panunga', 'Yara. Thedi. Anupunga da', 'Yaaru kitaiyavadu en em note irrukanu paarunga', 'Ans venum da', 'Any', 'Vennu annapa', '15 ans pls', 'Phys 11 mark notes elleam anapuga', 'Anapita da', 'Already', 'Class notes', 'Mechanical ena question padikanum', 'Teriyala', 'BCM pdf send pannu ga da', 'Question paper sent panuga da', 'Dei!! �', 'Dei Arounesh �delete pandra', 'Dei civil ans photo sent pannu da pls', 'Naa book left in class', 'Pls', 'Em 2 marks eruntha send panunga', 'Bm assignment diagrams anupunga', 'EM portion sent pannuga', 'Thara mit la keluda', 'Unit two three', 'Hydro thermal nuclear', 'Photo Send pandra', 'PDF LA erukum da', 'Pdf Panupu', 'Da', 'Hmm', '��', '�', '���', '��', 'Well done boy��', '���', 'Any one ku ans sollu ga da', 'Ans', 'Dei mokka podadha da', '6th one ah', 'Mm', 'Nandri��', 'Happy friendship day machan s', 'Happy frndship day', 'Happy amigoship déy', '❤️', 'Happy machans day', 'Appie friendship day machans', 'Happy friendship day da mama', 'Happy friendship day!!!', 'https', 'Cp record pdf yaarachum bachi irukingala', 'Cp ah', 'Hm mm', 'Maths test ku ans sent pannu ga', 'Maths test yellarukuma da', 'Mmm', 'Yellaray fail la yennna', 'Neeye failtha', 'illa da', 'Naan nalla dhaan yeluthuna', 'Nanum nallqtha ezhuthana', 'But fail �', 'Apa neeyum failthan da', '��', 'Dei but enum fail na yarrunu solla ve illya da', '���', 'Ellarukum than test', 'Nee passa da', 'Engaluku ennum sollala da', 'S na entha vati written good', 'Ama', 'Ohh.', 'I see', '�c', 'Enna da....nalaiku varuviya ila', 'Leave va', 'Varuvan da', '���', 'Ok da', 'Dei', 'Mut poi thongu da', 'Demonstration experiment send Panunga guys', 'Chem record index photo', 'Venum', 'Anyone', 'Nakku', 'Unga yarukitaiyavadu eg template irruta nalaiku edutu vanga', 'Che ex10 ku readings matum sent pannu ga guys', 'Dei bleaching power daex', 'Wait', 'Ok va?', '��', 'Adei', 'Poda angutu', 'https', 'English assignment send panunga', 'Yara mudijiruntha send panunga', 'Etha. Onnu na kuda anupu nga da', 'Dei 2nd own ah write pannanum ma??', 'Resume write pannanum ma illa atha pathi write pannanum ma', 'Chemistry graphs send plzzz', 'Anapungada', 'Nandri da sahatu', 'Eng assignment yaaravadu mudichingala', 'Ena assignmet da', 'English', 'No', '���', 'English la ena assignment da', 'Idu ellam', 'Ettana chapter mudicha', '170', '�', 'Dai na ippa than 89 ne varen', '�', 'Dei poi vera veleya paruga da', 'Same for you', 'Idhu..', '*Breaking News   இன்றிரவு 7', 'Wat is this?? �', 'Assignment', 'Eduvm panada da', 'Yen na nanga pannala yeduvum', 'Nakitu va', '���', '��', 'Confirm ahh pannalaya??', 'Panave illa toda kooda illa', 'Rocky sonna crctatha irukum', 'Dei panitu vanga DA. Elana ramya kathuva', 'Seri naliku lab irrukuma', 'Erukadhunu nenaikura', 'Dress edutu varava venama', 'Ena da ramya ku kiss kudukuriya', 'Un aalu ku needha kudupa..', '��', 'Ohh athu Avan aala', 'Yaaravdu eng assignment seiya poringala', 'Nee senja anupu da', 'Vaipilla', '��', 'https', 'Dae', 'Enna d', 'Workshop record mudichingala..', 'Collage irukka', 'Irukku', 'Tomorrow any dress code', 'Black da akash', 'Blue da', 'Black da', 'Seri ok', 'Black enkitta illa da', 'Dark or light blue', 'Any', 'Ok da', 'Dark blue', 'Y da dress codela', 'https', 'Yaaravdu eng assignment mudichingala', 'Nee mudichiya da', 'Illada', 'Kk', 'Good keep it up �', 'Yes sir! �', 'Innaiku Ms revision na', 'Aama', 'Ms qp vanthutha da', 'Dae cr qn paper eruka??', '@919789273239', 'S.', 'Iruka da?', 'Unit 5 notes eruka da MS', 'Sent pannuga', 'Refer the book...', 'Yaravadu unit 5 and 4 notes send panunga', 'Vera pdf irruka', 'No da', 'B sec class room irruku aana enaku download aaga matingudu', '�', 'All units 2 marks um send pannu', 'Dae', 'Xerox  potingana enaku serthu potu vanga.. da', 'Enakum', 'Enaku', 'Maths PDF send panunga', 'Yenda', 'Yaarum illanu nenaikiran', 'LinkedLn profile creation ', '6th unit annapuga', 'Notes anupunga da', 'Evs qp anupunga da', 'Seekiram da', 'Old qp', 'https', 'All the 1st  year students are instructed to join the above WhatsApp group immediately', 'Maths 2 marks classroomla irrukarudu send pannuga', 'Ohh', 'En da ohhh', '��', 'Dei enna da andha IBM etho meeting solli message ah poduraga', 'Nagana enum vittuke pola adhu kulla evola message', 'Is that important', 'To join the video meeting, click this link', '/t.meet/wiy-cgyx-axq', '�', "As tomorrow (31st Aug'22)  is the last date for registration for  the below 2 National level ICT Academy events - All the 1st year students are instructed to register for the same compulsorily before end of today", 'Edhu da apply pannalam', '��\u200d♂️', 'Puriyala da', 'Congratulations ��', 'Idhu enna da', 'Wt?', 'Pay pannanuma', 'Ama da', "Ma'am anupunadha?", 'Indha meeting', '??', 'Idhu rply pannan da', "Ma'am anupunadhu yaaravathu apply panningala", 'illa da', 'Inime than pannanum', 'Nee panniya', 'Nah', 'Nee pannumbodhu sollu nanum panra', 'Dai learathon panitan simple a than irruku panikonga', 'Paniten man', '�', 'Idha dhan learnathonla padikanum', 'Yarulem youth talk apply panna poringa', 'Naa', 'Ilaa', 'Epidi DA panrathu', 'Maths Divergens thorm question sent pannuga pa', 'Nandri', 'https', 'Guys print out pottachi', 'Rs 4', 'For EM question bank', '??', 'Nothing da', '. Mm', 'Dei yara', 'Maths imp anupunga da', 'Ennada ellarum padichitinga pola', 'Exam mrnga ila', 'Afternoon ah', 'Shaj Etha xerox eaduthutu va', 'Me also da', '.', 'Nane yedhupennanu double than', 'Hmm', 'Ok', 'Enakum', 'https', 'Dae em write pannanuma..', 'Revision sums la...??', 'illa da', 'https', 'https', 'Dei', '��', '.', 'Wait', 'Comming', 'Another video', "Ya it's dangerous one ���", 'Nayagan meendum varar', 'Tomorrow once upon a time release', 'Mm okkk super', 'Super naliku once upon time', '.', 'Da akash', 'Kandipa podu video', 'Yaaru ellam em mudichinga', 'Yarum ila', 'Dae', 'Em mudichingala?', 'Noo', 'Mrng padichikalam', 'Exam apa?', 'forenoon or afternoon..', 'Af', 'Shield', 'New add', 'Link anupu', 'Da', 'English all units PDF send panunga', 'Unit 2 mattum illa', 'Tmrw lab dress eaduthutu varanuma', 'Venam da', 'English padichitingala da', 'Eng thanna pathukelam', 'Phy lab dha na inaiku?', 'Unakennapa...topperu', 'Nanga apadiya', '���', 'Yaaru nana romba peeumiya eruku�', 'Dei university pratical time table sent pannuga da', 'Adhuku?', 'Short procedure elathukum padikanuma?', 'Ni ombu', 'Apadi Orama poi oombu ', 'Unfortunately earth is round', '��', 'Thara paravasa nilaiku poitinga pola..??', 'Dae', 'Nalaiku  workshop eruka namaku.', 'Cr soldra', 'Iruku da naliku', '1.10 la naliku crt ha assemble agidanu', 'Dae', 'Nalaiku shoe potutu varanuma..', 'Ethuku eduthutu va', 'Ok..', 'Phy mannual sent pannu ga', 'Ama naliku edavadu padikanuma illa suma vandale poduma', 'Therilayae', 'Sir Ku msg pani kelu da', 'Avalovu vegam', '�', 'Dai delete panitan paatiya', 'Pathutan', 'Rendu parum oray time la anupunanga pathela', 'Seri nee vaya mudu..', 'Dai evanagu anapcha vegatula whatsApp server down aiduchi pola', 'Dae kuzubhumbu', '�', 'Dai arounesh unaku teriyuma', 'Summa va da', '���', 'Dae cr ketu soldra', 'Arish oru 5 avuthu Padi da', 'Akash punda', 'Etha akash pundaya', 'Hmm', '���', '�', 'Dae', 'A sec em qn paper anapunga', 'Da', 'Physics lad epidi erunthuchu', 'Kadupa ahh erundhu dhu', 'Write panitiya', 'Asokan sir vanthara', 'Yaaravadu em qns paper send panuga', '15 qns mudichingana anapunga', 'Physics LA entha experiment padikavena', 'Theriyala pangu ��', 'Ethana peru EM pottinga', 'Naa podala padi than pota A section qns paperla irundy', 'Dei arish naliku eduthutu varatha', 'Yarumey podala da', '�', 'Ennathu dq', 'Che practical mannual sent pannu ga', 'Cod dissolved o2 ku short procedure table mattum dhan yeluthanuma da??', 'Vera yenna yelithanum??', 'Aama', 'Aim ch req venama', 'Vena  formula padi', 'DO ku short procedure sent pannunga', 'Dai yaravdu ms important qns anapuhada', 'Yar yarula iruntha', 'Idu yarukitaiyavadu irunda anapuga', 'Thara ,akash,arish,siva', 'Bala badam pal kudichitu bhothaila eruntha', '�\u200d�', 'Sir note LA write pana all questions da', 'Okk', 'Atha anupu da', 'Enaku venum', 'Goya pazha saptu bodhai yaa erundha', '*thara', 'Ans anupungada yara', 'Dei', 'Ethukuda ithelam', 'Tmrw college eruja', 'Eruka', 'Therila', 'Mala akka kita kelu', 'Illa da', 'Yaar na hall ticket vangaliyo avanga dhan ponum', 'Ok', 'https', 'Deii', 'Sem namba batch ku ena time nu theriyum ha', 'Apo ena time', 'Sekaram sollunga da', 'F. N 9.30', 'Maths important 11 marks erntha send panuga', 'Any one having my calculator', '*nope', 'Un calculator un urimai....', 'Frnds', 'Entha chapter chinnathu', '5unitsla', 'Sollunga', 'Maths a', 'Ss', 'Athana', 'Exam', '5  unit', 'Aparm', 'Vera etha oru unit sollu da', '1 unit ellame similara than errukum', 'Adu easy', 'Vera', 'Athu rendu finished', 'Vera sollu', '3 unit', 'Hn ok da', '2 marks pdf sent pannu ga da', 'Maths', 'Hello��', '???', 'Enaku...yara....thiruchitrampalam', 'Padam anupunga', 'Hd print', 'Telegramla', 'Yen da na maths padike kekaren anapula padam kekariya', '1st maths sent pannu da', '..', 'Padida venna', 'Not that', 'Vera ila', 'Stokes theorem last cube sum send panunga', 'Ss anupunga', 'Sem time table anapunga', 'Nee malla enña paninga', 'Cr', 'Restroom TV LA padpathutu eruntherupa', '��', 'null', '1 of our old 1�', 'Dae ena edhu', 'Paru', 'Adho eruku..', 'Maths yaravathu mudichingala', '�', 'Illa buddy', 'Nee mudichiya..', '??', 'Ethulam palasu', 'Ella 2 adicha', 'Dae ena keta enna soldra..', '2 chapter muducha da', 'Ohh..', 'Mmbu', 'Nee poi umbuu..', 'Rendu perum athukuthan da laiki', 'Aii onga vedu address solu da', '��', 'null', 'Onaku oru vibrator vangithara da onaku thevapadum', '���', 'No need ra', 'Neeye vachiko', 'Oa vaila vachi veda va da', 'No thanks da', 'Adha bala ku vangi kudu pavam', 'null', '�', 'null', 'Ball', 'null', 'null', 'null', 'Imp aa da', 'Dae revision la nama cls write pannangal adhu', 'Imp ha da mohan', '�\u200d♂️', 'Ila', 'Ss', 'Ok da', 'Mohan', 'Sabarish classla sonnanga', 'Da', 'Kandippa itha padicha 3to 4 11m attend panalama', 'Ans matum yara anupunga da', 'Plzz', 'Super da mohan thanks da', 'Unit 4 important sums eruntha send panunga', 'Ans anupunga da plzzz', 'Enna da edhu', '??', 'Imp da', 'For university', 'Yaru da send pana', 'Robotics dept da', 'Frnd', 'Ohh avana', 'Inverse laplace convolution nu mention pannalana partial fraction method la podalama', '??', 'Hm bookla paaru', 'Enakum sollu', 'Book la illa da', 'Apa anthq method laiyr podu', '3 unit than etuku', 'Nxt 2', '5 units um iruku da olunga paaru', '11 mrks la 3 than eruku', 'Paaru', 'Sem enna time st agum??', '10.00', '9.30 illa', 'Ya', 'Da', 'Ila man...hall kulla nee .9.30kulq..irukanum', 'Crt ahh oru time sollunga', '7.02 da', 'Un vaiyla blurr uhh pun*** da', 'Thappu', '7.04', 'Seriya ana cringe la erukae..', 'Aakash sticker nalaiku vida padum..', 'Sutha mudra su**i', 'Nee thiruntha matala', 'Adhan delete panitan la aprm enna oanku', 'Palkova', 'Inda fight semaiya irrukum aana comicla majin boo vara matan', 'Ithaliyum avan vara matan da', 'Editing mistake', 'Avanuku pathila frieza varuvan da', 'Hmm', 'Dei yarula maths finish', 'Mee', 'Naa ila', 'Oh ok', 'Any imp....', 'Good', "Ya it's from fourth unit", 'Nope', 'Dei easy thada sekaram parunga', 'Nalla pannunga ellaru', 'Dae', 'Timing', 'Enna sum', '..', 'Solunga', 'Hm tq da', 'All S grade students go and study', 'Antha denominator la s^2', 'Timing solu da', 'Nu varu paru atha', 'S grade kamala..', 'Oh ..ok.... gold medalist', 'Okiee', 'Dae', 'Timing sollu da', 'Mrng to afternoon', '10 o clock exam da', 'Adhukula vandhudu da', '9.30 ku la hall erukanum ahh', 'Therila bro', '9 45 ku', 'Bro', 'Enna  pudhusa broo s grade kamala..', 'Summa bro', 'Free fire la kuptu kuptu bro bro nu varudha...', 'Bro game delete pannitan bro', 'No game', 'Ohhh ..thirunthitiya bro', 'Exam aprm install panniduvan bro', 'Nee thirunthavey mata bro', 'Exam time table sent pannuga', 'Apa confirm ahh s grade dha', 'Ya bro nee vera', 'Epo dha padika va start pannirukan', 'Ok bro', 'Y bro', 'Yaru kitalum idha dha solluriga', 'En Peru gnanam', 'Vunmai ya dha bro solla mudiyum', 'Dae', 'Ponga da ..', 'Pathukalam..... pathukalam... results varum pothu theriyum', 'Neenga poi duet padunga ponga', 'Neenga ....vanthu', 'Offline poitunga', 'Click panna maten da', 'Ss anupava', 'Pathikiriya', 'Net ila� download panna mata sorry', 'Adhan da screen shot', 'Anupavanu ketan', 'Athatha download panna net illa', 'Olan edho type pandrar', 'Adha hd print uhh vandhuchu la en inum theatre print la anapura', 'Adhu naa edhu thadhu theatre la', 'Un kitta pesi naa time waste panna virumbala naa poi padikura', 'Kelambu kathu varetum', 'Dei pona sem Ku important sums vanthuchula athumeri send panung da', 'Vanthuchuna', 'Nee padichita solra', 'Nanga apadiya', 'Tomorrow (14.09.2022) morning the  following Bus numbers are operated', 'null', 'null', 'https', 'Siva', "I'm very sorry", 'Siva yenna pannuvan theriyuma itha pathutu', '�', 'Dei enaku calculator', 'Venum', 'Yara extra vachiruntha', 'Thanga', 'Illa da en kita..', 'Kk', 'Okk', 'Any important??', 'Thrla', 'Mohan kitta kellu da', 'En kita ilq', 'Ethana chapter padicha', 'Ms da', 'Atha...enna lesson la padicha', 'null', '��', 'Padichitiya da', 'Fulla', 'illa da', 'Aparm evalo padicha', '3 units da', 'Nee', 'Onnu kuda ila', 'Veliya vanturuka', 'Ohh ....ellathaiyum padichiyq ila...imp mattum ma', 'illa da', 'All', 'Hm ok da', 'Padichitiya pallu', 'Akash ella 11 mark ha paducha', 'illa da sir class la nadathunathu mattum da', 'Ok da', 'Sir sonathu thana paducha', 'Ama da', 'Ok da', 'MS ku yedha vidhu material erundha sent pannu ga da', 'Charge carrier concentration intrensic semi conductor 11 mark anapugada', 'Hall a da', 'Sir write panna notes ahh illa ms book notes venuma?', '?', 'Light potu yedu da', 'Dei ferromaganetic material notes anapunga da', 'Imp and easy 3 lessons sollu', 'Imp and easy 3 lessons', '??', 'Example', 'Sollitan da', '??', 'Pdf edhum illa', 'Ila', '.', 'Thanks da Aakali�', 'Dei...poi padida', 'Poda', 'Gm', 'Yaar exam ku padichitinga', 'What are High temperatures Superconductors? Explain the structure, Synthesis, properties and applications of 123 superconductors', 'Inda qns answer yaarukitaiyavadu irruka', 'Textbook la irukum', 'Photo edu anapuriya', 'Enkita book illa', '��', 'Intha questions varuma da', 'Teriyala', 'Hmm', 'Any imp.?', 'Dei anupu da', 'Padika pora', 'Yelathiyum padi da', 'Nee ethana lesson mudicha', 'Padikavay illa da', 'Inemay dhan', 'Hm good', 'Ivalo neram ennatha nakkuna', 'Dei ethemeri tha question send panringa but Entha question num.varamatuthu', '���', 'Read all fuck all', 'Hm ok dude', 'Evs PDF send panunga', 'Edhan en kitta erukudhu', 'Classroom la irruku paaruda', 'College Ku epo poga mudiyathu da', 'Seri school ku poda', 'Okva', 'This is inhalf to pass', 'Adhu inhalf illa dude', 'Enough', 'Neenga petertha', 'Ponga', 'Unit 1&2 notes anapunga', 'Three notes hum anapunga', 'https', 'Padichitiya da', 'Unakennapa padichita', 'https', 'https', 'https', 'https', 'Thambi imp ketaney', 'Anupupa', 'Ni tha anapanu', '��', 'Enkitta ilada', 'Akash', '@919150232682', 'BM ku any important question', 'Anupu da', 'Ama da', 'Dei yadha vidhu sent pannuga da BM ku', 'BM oru unit oda first half padicha matum podumla', 'Who gave da', 'Frd da', 'Class grp la potutu da', 'Nana', 'Naanay potutan da', 'Rajiv Gandhi la ya koduthanga da', 'Ama da', 'Etha padicha pothuma', 'Edha full ahh padichitya?', 'Hmm', 'Molding matum padikanum', 'Seri padi', 'Read all fuck all', 'Ithu ethuku da', '�', 'Pushup pana', 'Evolo', '700', 'Oh okok', 'Eduku?', 'Dei anime patha Periya ��agamudiyathu da', 'Ena DA mrng aramichitinga', 'Bme pdf anupunga da', 'Sir koduthathu', 'Pona sem em question paper eruntha send panunga', 'https', '???', 'Em eathathu send panunga da', '�', '�', 'https', 'https', 'Otha eru da sticker vangitu vara', 'Na already vangikunu dhan da irukan punda', 'Onaku varum parru', 'Entha photos Ku sticker ready panravanguku life time settlement', 'Enna da ithu', 'Evano ponna sem EM q/p kettane', 'Adhan ethu', 'Imp iruntha anupungala da', 'Dei', 'Yara. Anupunga da', 'Iruntha anapa matoma da', 'Hm', 'Third unit la x bar y bar kandupidikka formula irrukumla ada anpuga', 'For regular shapes', 'Athu kulla third unit vantiya', 'Illa da frnd ketan', 'Ohh �', 'Anapugada', 'Ila bro.   Veetuku poitu anupura', 'Dai motam 10 per msg patu irrukanuga avanuga kitaium than kekuran', 'Ethuva da', 'Ethuva', 'Hmm ✌�', '��', 'Edha eppidi solve pannu redhunu solluga da pls', 'Repeat ed sums these 2 models', '�', 'Imp da', 'Need answers', 'Hn anupu da', 'Nee anupu da', 'Venum nu ketan da', 'Ohh', 'Ok da', 'Yenga sir kodutha thu da', 'Namba sir eppada kudu taru', 'Ethula unit 4 and 5 matumtha eruku', 'College la yellam ketanga arrer pasanga appo kodutharu', 'Yen frnd arrer avan dhan koduthan', 'Na orurhana anupuran Avan Pannu va', 'Ivan dhan adhu', 'Harry while sighting MBA akka', 'Na eppa da adha ippadi parthan', 'https', 'https', 'https', 'https', 'https', 'https', 'It will be usefull', 'Thnx bro', 'https', 'Model qn paper send pannungada', 'Em..', 'Thank you buddy', 'null', 'null', '�', ', ���', '��', 'Prepare aagitiya da??', 'S', 'null', 'Who was', 'This', 'Dei siva y this kolavari�', 'null', 'Unknown�', '�', 'Illa da', 'Mayiruh oru thadava delete panna ok nee ellar chat delete pannikite irundha', 'null', 'Watsapp beta version da', 'Admins nu yar chat vena delete panra power iruku', 'Naanu admin da', 'Ohh apadiya', 'Ipa paaru oru demo katra', 'Mela paaru da', '�mohan it deleted', 'null', 'Edho eppadi', '�', 'D ei long press panni delete pannu', 'Simple', 'Only delete for me option than irruku', 'Update panra motha', 'Illa da delete for everyone varum', '��', 'Kadasiya eppa panniyo��', 'Dei update panni ya', 'Wats up ah', 'Hmm ongoing', 'null', 'Oh ok', 'Okk done�', 'Poi ellam padinga da', '�yen message than 1st ah', 'Dei ���', 'Nee thana tha guru enaku', 'Dae yaaru sahaj ahh admin ahh podadhinga', '��', 'Naa enna da panna', 'Balls', 'Poii padi poo', 'Enna da�', 'Poi padi da', 'Seri Seri', 'Important?', 'Idhula first sum answer correct a paarunga', 'Crct ra', '✌�', 'Meethi sumla anupu', 'Onu dan potan', 'So sad', '��', 'English send panunga boys', 'English', 'English. ���', 'Okva', '��', 'Timing da�', 'null', 'No more that sticker plz', 'Y', 'Ni naku', 'null', 'Dei summa iru da', 'Adhu over da', 'Hari', 'Siva in Anniyan mode', '�', 'https', '�����', '�', 'Bye bye', '��', 'Enna aven poi tan', 'Eru', 'Avenna add pannu ga da', 'Waste of time', 'Avanthan ai/ml poiduvanla atan ippave left aitan', 'Naliku oru naal than cse la irrupan', 'Yen', 'Msg panalum reply pana maturada', 'Hmm...', 'Call pana edukala', 'Vidu', 'Ena achi da', 'Nalaiku varuvan la pathukalam', 'Small boys fight', 'Yaruku', 'Poi chat padi', '�', 'English pdf send panuga da', 'Yaru da', 'Hari da', 'Seri da english pdf da', 'Dei nippatunga da', 'English important question send Panunga', 'Podhum da', 'Rajiv gandhi paiyan ta ketu iruka send panana send panura', 'Marakama anupu da neeye othudadha', 'Ponnu kulikarama madiri iruntha podu', 'Un video va Kekala da', 'Pradeep �', 'Dei pradeep mokka vanga nana me apadiya�', 'Saturday', 'Seniors sonnaga', 'Avan td exam attend panala', 'Yen da', 'En da', 'Po poi world record la aluthu po', 'Bus eari oditan', '�', 'Vidu avennu ku kuduthu vechadhu adhan�', 'Apo namala eamathitanga', 'Hmm', 'Bala pass aa da', '�\u200d♂️', 'Aaiduvanu solran', 'Aven aiierun dhu van da', 'Gods of destruction layum hari leave agitan', 'Akash vitu pinadi erupan', 'Puriyal da', 'Ama da', 'Puriyala da', 'Theliva a sollu', 'Thannila bag mattum medhakum nu sonna na la adhaan', 'Sema late response da gn', 'Dai na epa dha da patha', 'Hmmm...', 'Olunga', 'Imp send panalaya', 'Rajiv gandhi clg la', "Ma'am ah kelu da", 'Qns bank qns ellam epadi ketu irrkanga', 'Pakala da', 'Model keata maari ya illa normal irrka', 'Pakura iru', 'English pdf send pannu da', 'Classroom la irruku paaruda', 'Clg ponuma ithukagq', 'Aprm padika venama', 'Oh ok da... parama padida', 'What is your name', 'Mohan IT', '�', 'Mm', '�', 'Unit 2 eruntha send panunga', 'Aprm 2marks', 'Classroom  la  eruku paaru da', '*Google classroom', 'WHO send this', 'Frnd', 'Yevalovu days leave', 'Letter aa photo yedithu anupunga da', 'Therila da', '28.9.22 college']



trainer.train([
    'Hi',
    'Hello',
    'I need roadmap for Competitive Programming',
    'Just create an account on GFG and start',
    'I have a query.',
    'Please elaborate, your concern',
    'How long it will take to become expert in Coding ?',
    'It usually depends on the amount of practice.',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])



#trainer.train(t)
'''


from chatterbot import ChatBot
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

bot = ChatBot('Bot')

contact=input('Enter the saved name or number of the person you want to auto-chat:')


#Uncomment the below line if you are yet to install chrome driver (or) download it from https://chromedriver.chromium.org/downloads

from selenium.webdriver.chrome.service import Service; from webdriver_manager.chrome import ChromeDriverManager; driver=webdriver.Chrome(ChromeDriverManager().install())



#driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")

while True:
    try: search_box=driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
    except: continue
    break
     
def fun(contact):
    driver.maximize_window()
    search_box=driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
    search_box.click()

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.send_keys("a")
    actions.key_up(Keys.CONTROL)
    actions.send_keys(contact)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    try:
        #chat=driver.find_element(By.XPATH, "//span[@Title='"+contact+"']")
        chat=driver.find_element(By.CLASS_NAME, "_3OvU8")
    except:
        try: chat=driver.find_element(By.CLASS_NAME, "_8nE1Y")
        except:
            driver.minimize_window()
            contact=input('no such contact found. please re-enter contact name/number:')
            fun(contact)
    chat.click()

    try: last_sent_message=driver.find_elements(By.CLASS_NAME, "_27K43")[-1].text.splitlines()[-2]
    except IndexError: last_sent_message=''

    while True:

        messages=driver.find_elements(By.CLASS_NAME, "_27K43")

        try: message=messages[-1].text.splitlines()[-2]
        except IndexError:
            actions = ActionChains(driver)
            actions.send_keys("sorry, I'm unable to comprehend emojis")
            actions.send_keys(Keys.ENTER)
            actions.perform()
            last_sent_message="sorry, I'm unable to comprehend emojis"
            continue

        if message!=last_sent_message:
        
            response=bot.get_response(message)

            actions = ActionChains(driver)
            actions.send_keys(str(response))
            actions.send_keys(Keys.ENTER)
            actions.perform()        

            last_sent_message=str(response)
fun(contact)
