echo Deploy de $HOST
echo $CI_REPOSITORY_URL
echo git@gitlab.com:$CI_PROJECT_PATH
echo branch: $CI_COMMIT_REF_NAME
echo Listando pasta de sites:

ls -la
if [ -d $HOST ]
then
    echo Existe o diretório $HOST
    cd $HOST
else
    echo Não Existe o diretório $HOST, criando...
    sudo mkdir $HOST
    cd $HOST
fi  

if [ -d .git ]
then
    sudo git remote set-url origin $CI_REPOSITORY_URL
    sudo git remote -v
    sudo git checkout $CI_COMMIT_REF_NAME  
    sudo git pull origin $CI_COMMIT_REF_NAME
else
    sudo git clone $CI_REPOSITORY_URL .
    sudo git checkout $CI_COMMIT_REF_NAME
    sudo git pull origin $CI_COMMIT_REF_NAME
fi

# Entrando no ambiente virtual
source /home1/filipelo/.venv-filipeelore.love/bin/activate
# Instalando dependências
pip install -r requirements.txt

exit