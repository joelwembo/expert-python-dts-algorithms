
git add .
git commit -m "Data Structure update 04/11/2021"
if [ -n "$(git status - porcelain)" ];
then
 echo "IT IS CLEAN"
else
 git status
 echo "Pushing data to remote server!"
 git push -u origin master
fi

read

exit
