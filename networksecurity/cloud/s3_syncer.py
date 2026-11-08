"""
Hum ye kaam isliye kar rahe hain taaki hamare
Network Security ML project ke training outputs aur final trained model ka backup AWS S3 cloud storage mein rahe. 
1) artifacts folder 
2) final model folder

2. s3_syncer.py kyun banaya?
Is file mein humne S3 ke saath communication aur file synchronization ka reusable logic rakha hai.

For example, maan lo humein 3 different locations se data S3 par upload karna hai.

Agar har jagah AWS upload ka code likhenge, toh code repeat hoga.

""" 

"""
 Iska real-world benefit kya hai?
Maan lo tumhara laptop crash ho gaya ya tumne project kisi doosre server par deploy karna hai.
- Training artifacts S3 mein available rahenge.
- Final trained model S3 mein available rahega.
- Different training runs ke models timestamp ke according separate rahenge.
- Future mein deployment server S3 se model download kar sakta hai.
Ek important baat: S3 mein upload karne se model automatically deployment ke liye ready nahi hota. 
Deployment ke waqt model ko S3 se download/load karne ka logic bhi chahiye.

"""


import os


class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)
