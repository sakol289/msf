unzip ngrok.zip
mv ngrok /$HOME/msf
pip install alive-progress
pip install tqdm
apt install neofetch
apt install figlet
apt install lolcat
apt update
apt -y upgrade
apt -y install git ruby ruby-dev make clang autoconf curl wget ncurses-utils libsqlite-dev postgresql postgresql-dev libpcap-dev libffi-dev libxslt-dev pkg-config
gem install bundler
gem install nokogiri -- --using-system-libraries
bundle install --gemfile Gemfile.local
apt install wget -y
curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz
gunzip metasploit_5.0.65-1_all.deb.gz
dpkg -i metasploit_5.0.65-1_all.deb
apt -f install
pkg install unstable-repo
pkg install metasploit
mv ngrok $HOME/msf/system/ngrok
termux-setup-storage
