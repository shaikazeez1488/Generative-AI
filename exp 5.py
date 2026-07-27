from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

cv = CountVectorizer()
vectors = cv.fit_transform([text1, text2])

similarity = cosine_similarity(vectors)[0][1]

print("Cosine Similarity:", similarity)

if similarity > 0.8:
    print("Documents are highly similar.")
elif similarity > 0.5:
    print("Documents are moderately similar.")
else:
    print("Documents are less similar.")