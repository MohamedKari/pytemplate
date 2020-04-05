set -e

reponame=$1

if [ -d "$reponame" ]; then
  echo "Directory '$reponame' already exists. Please choose a different reponame or delete it first and then re-run."
  exit 1
fi

git clone --depth=1 --branch=master https://github.com/MohamedKari/pytemplate.git $reponame

cd $reponame
rm -rf .git
make init-repo
rm -f ../$0