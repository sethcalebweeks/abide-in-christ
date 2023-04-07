import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
Translate the following paragraph into modern English that is simple to read while preserving the meaning of the original text.
Leave the word 'abide' as is, because that's the title of the book. It is VERY important that you do not change the word 'abide' to 'stay' or 'remain' or any other word.
Break up long sentences into shorter sentences, and use contractions.
Use modern words and grammar, and make sure each sentence is easy to understand.
Replace any Bible verses with the exact ESV translation.

Paragraph:
"As the Father hath loved me, so I have loved you. Abide in my love, even as I abide in my Father's love."-JOHN 15:9,10.

Traslation:
"As the Father has loved me, so have I loved you. Abide in my love. If you keep my commandments, you will abide in my love, just as I have kept my Father's commandments and abide in his love." - John, 15:9,10

Paragraph:
CHRIST had taught His disciples that to abide in Him was to abide in His love. The hour of His suffering is nigh, and He cannot speak much more to them. They doubtless have many questions to ask as to what that abiding in Him and His love is. He anticipates and meets their wishes, and gives them HIS OWN LIFE as the best exposition of His command. As example and rule for their abiding in His love, they have to look to His abiding in the Father's love. In the light of His union with the Father, their union with Him will become clear. His life in the Father is the law of their life in Him.

Traslation:
Jesus taught His disciples that to abide in Him was to abide in His love. He was about to go to the cross, so He couldn't say too much more to them. They probably had many questions about what it means to abide in Him and His love. Before they could even ask, He gives them HIS OWN LIFE as the best explanation for His command. As an example and rule for their staying in His love, they had to look to His staying in the Father's love. In the light of His connection with the Father, their connection with Him would become clear. His life in the Father is the law of their life in Him.

Paragraph:
{}

Traslation:
"""


def modernize(paragraph):
  response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt.format(paragraph),
    max_tokens = 3000,
    temperature = 0.7
  )
  return response.choices[0].text.strip()


for line in open("original/chapter-23-as-christ-in-the-father.txt"):
  modernized = modernize(line)
  open("book/chapter-23-as-christ-in-the-father.md", "a").write(f"{modernized}\n\n")

