set -e

reponame=$1

if [ -d "$reponame" ]; then
echo "Directory '$reponame' already exists. Please choose a different reponame or delete it first and then re-run."
exit 1
fi

if [[ ! $reponame =~ ^[a-z][a-z0-9_]+$ ]]; then
echo "Please choose a repo name with
- only lower case letters (Docker requires container-tags to be in all lower case), 
- underscores (packages with dashes cannot be imported by python), and 
- numbers. 
These rules are enforced ensure consistent naming accross the project."
exit 1
fi

git clone --depth=1 --branch=master https://github.com/MohamedKari/pytemplate.git $reponame

cd $reponame
rm -rf .git
make init-repo
rm -f ../$0