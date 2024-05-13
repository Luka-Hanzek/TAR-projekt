import os
import urllib
import tarfile
import gdown


def get_MAVEN(out_dir):
    print('Downloading MAVEN dataset')

    gdown.download_folder(id='19Q0lqJE6A98OLnRqQVhbX3e6rG4BVGn8', output=out_dir)


def get_RAMS(out_dir):
    print('Downloading RAMS dataset')

    file = "https://nlp.jhu.edu/rams/RAMS_1.0c.tar.gz"
    ftpstream = urllib.request.urlopen(file)
    file = tarfile.open(fileobj=ftpstream, mode="r|gz")
    file.extractall(out_dir)


def main():
    datasets = (
        (os.path.join(os.path.dirname(__file__), 'MAVEN'), get_MAVEN),
        (os.path.join(os.path.dirname(__file__), 'RAMS'), get_RAMS),
    )

    for dirname, download_func in datasets:
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        if len(os.listdir(dirname)) != 0:
            print(f'Directory {dirname} is not empty. Delete contents and continue with download (Y/n): ', end='')

            skip = None
            while skip is None:
                resp = input().strip()
                if resp in ('', 'y', 'Y'):
                    skip = False
                elif resp == 'n':
                    skip = True
                else:
                    skip = None

            if skip:
                continue

        for root, dirs, files in os.walk(dirname, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        
        download_func(dirname)


if __name__ == '__main__':
    main()
