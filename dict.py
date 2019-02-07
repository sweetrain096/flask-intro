from flask import Flask

dict = Flask(__name__)

@dict.route('/')
def hi():
    return "딕셔너리 첫페이지입니다."

@dict.route("/dictionary")
def dictionary():
    return "검색해보세요"
    
@dict.route("/dictionary/<string:word>")
def word(word):
    word_dict = {
        "apple" : "사과",
        "cherry" : "체리",
        "banana" : "바나나"
    }
    if word_dict.get(word) :
        return f"{word}는 {word_dict[word]}!"
    else :
        return f"{word}는 나만의 단어장에 없는 단어입니다!"
    
    
    
if __name__ == "__main__":
    dict.run(host='0.0.0.0', port='8080', debug=True)