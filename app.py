from nltk.tag import CRFTagger
import json

def split(msg):
  return msg.split()

def tagger(msg):
  ct = CRFTagger()
  ct.set_model_file('model/all_indo_man_tag_corpus_model.crf.tagger')
  hasil = ct.tag_sents([split(msg)])
  return hasil[0]

def SortTuple(tup):   
    tup.sort(key = lambda x: x[1])   
    return tup  

def JsonResult(arrResult):

  sorted = SortTuple(arrResult)

  x = -1
  lastTag = ""
  ww=[]
  tag=[]

  for i in sorted:
    if lastTag!=i[1]:
      x=x+1
      lastTag=i[1]
      ww.append([])
      ww[x]=[]
      ww[x].append(i[0])
      tag.append(lastTag)
    else:
      ww[x].append(i[0])

  tmp='{'
  for i in range(len(tag)):
    tmp=tmp+'"'+tag[i]+'"'+':['
    for j in range(len(ww[i])):
      tmp=tmp+'"'+ww[i][j]+'"'
      if j<len(ww[i])-1:
        tmp=tmp+','
    tmp=tmp+']'
    if i<len(tag)-1:
      tmp=tmp+','
  tmp=tmp+'}'

  result=json.loads(tmp)
  return result


# main

from flask import Flask, url_for, request, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/')
def api_hello():
    if 'msg' in request.args:
        return JsonResult(tagger(request.args['msg']))
    else:
        return '{"status":"error","message":"please input message"}'

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=5055)