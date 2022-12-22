from flask import Flask, request, render_template
import pickle
import random
from model import word_per_lang, clean, vectorize

# Parameters
label2Lang = {
    "eng": "English",
    "rus": "Russian",
    "deu": "German",
    "hin": "Hindi",
    "spa": "Spanish",
    "fra": "French",
    "ara": "Arabic",
    "ben": "Bengali",
    "urd": "Urdu",
    "por": "Portuguese"
}
test_sentences = ["Lebe, wie du, wenn du stirbst, wünschen wirst, gelebt zu haben.",
                  "Denke an all das Schöne, was in dir selbst und dich herum wächst und sei glücklich!",
                  "Wie groß wäre die Amortisationszeit des Prozesses unter veränderten Bedingungen?",
                  "Abzweigdose für Leitungen zur Aufnahme von elektrischen Kabeln",
                  "Esperame un rato que tengo que reiniciar el modem",
                  "¿Conoces algún lugar cerca donde podamos hablar tranquilamente?",
                  "No me vengas con esto ahora.", "Parece que fue ayer, ¿no?", "¡Cuánto tiempo sin verte!",
                  "¡Qué bien te ves!", "কারো সাথে ভাগাভাগি করলে সমস্যা অর্ধেক হয়ে যায়",
                  "ভালবাসার নৌকা পাহাড় বইয়ে যায়।", "নয়নের মণি",
                  "এই ভাষা যথেষ্ট নয়", "أهلاً", "لا تقلق", "كيف أصل إلى هناك، من فضلك؟", "أراك في المرة القادمة",
                  "مساء الخير",
                  "It's never been my responsibility to glaze the donuts.",
                  "There's an art to getting your way, and spitting olive pits across the table isn't it.",
                  "There's an art to getting your way, and spitting olive pits across the table isn't it.",
                  "We should play with legos at camp.", "The events transpired in an unfortunate manner",
                  "L'invention constitue donc un dispositif miniaturisé économique.",
                  "Chaque participant peut soumettre jusqu'à cinq photos par concours.",
                  "Je souhaite soumettre une œuvre VR.", "Hello! My name is Abderrahman! I like potatoes ",
                  "This notion is beyond preposterous. I shall return to Liverpool and watch my beloved team play.",
                  "تو شاہیں ہے پرواز ہے کام تیرا ترے سامنے اور بھی ہیں",
                  "عروجِ آدم خاکی سے انجم سہمے جاتہ یہ ٹوٹا ہوا تارا مہ کامل نہ بن جائ",
                  "بھری بزم میں راز کی بات کہہ دی",
                  "Quem vê cara não vê coração", "Quem não arrisca não petisca",
                  "Você deveria pedir um aumento de salário",
                  "Quem não arrisca não petisca!", "Aqui se faz, aqui se paga", "Cada macaco no seu galho",
                  "Доверяй, но проверяй",
                  "Мой дядя самых честных правил", "Не хочу учиться, а хочу жениться!",
                  "Тварь я дрожащая или право имею",
                  "Любовь зла, полюбишь и козла"]


# Import pickle model
model = pickle.load(open("mnbayes.pkl", "rb"))
bag = []
with open('bag.txt', 'r', encoding='utf-8') as file:
    bag = file.read().splitlines()

# Initiate flask app
app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.form['action'] == 'pick':
        randIndex = random.randint(0, len(test_sentences) - 1)
        chosenText = test_sentences[randIndex]
        return render_template("index.html", random_text=chosenText)

    elif request.form['action'] == 'identify':
        feature = [str(txt) for txt in request.form.values()]
        ident = "Detected Language: {}."
        if feature[0] == "":
            ident = "No text was given as input!"
        else:
            vector = [vectorize(clean(feature[0]), bag)]
            ident = "Detected Language: {}.".format(label2Lang[model.predict(vector)[0]])

        return render_template("index.html", identified_lang=ident)


if __name__ == "__main__":
    app.run(debug=True)

