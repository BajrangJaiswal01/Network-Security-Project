"""
. Batch Prediction ka use kyun hota hai?
- Large datasets ko process karne ke liye.
- Multiple records/inputs ki prediction ek saath karne ke liye.
- Automated security scanning mein.
- Har record ke liye alag-alag prediction calls karne ki zarurat kam karne ke liye. 


Bahut saare input records par ek hi baar mein prediction karna = Batch Prediction.

Example:
- 1 URL → Single Prediction
- 100 URLs → Batch Prediction
- 10,000 URLs → Batch Prediction

"""