my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def dictionaryTuples():

    newArray = zip(my_dict.keys(), my_dict.values())
    print newArray


dictionaryTuples()
