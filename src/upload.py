import boto3
import argparse
s3 = boto3.client("s3")

def upload_data(args):
    s3.upload_file(args.input_file_path,args.bucket_name,args.output_file_path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload data to S3")

    # add argument
    parser.add_argument("input_file_path", type=str, help="local path for uploaded file")
    parser.add_argument("bucket_name", type=str, help="s3 bucket name")
    parser.add_argument("output_file_path", type=str, help="output path for uploaded file")

    args = parser.parse_args()
    upload_data(args)






# s3 = boto3.client('s3')

# s3.upload_file('nw-yifeng','lyrics.csv','spotify_track_data.csv','wiki_hot_100s.csv')