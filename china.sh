#!/bin/sh

trap '' INT TSTP QUIT TERM

printf "\033[31m"
timeout 2 ./a.out
printf "\033[32m\n"
for i in $(seq 1 20); do
    sleep 0.2
    pct=$((i * 5))
    btc=$(awk "BEGIN {printf \"%.7f\", $i*0.00001287}")
    bar=$(printf "%-${i}s" "#" | tr ' ' '#')
    printf "\r[%-20s] %d%% Bitcoin miner %s BTC" "$bar" "$pct" "$btc"
done
echo -e "\n"
echo "BITCOIN MINING OPERATION COMPLETE!! THANK YOU CHINESE CITIZEN +100000 SOCIAL CREDIT"
printf "\033[33m"
echo "⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿"
echo "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿"
echo "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿"
echo "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿"
echo "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿"
echo "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿"
echo "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
echo "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿"
echo "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿"
echo "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿"
echo "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻"
echo "⠟⠋⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄"
echo "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄"
beep() {
    case "$OSTYPE" in
        msys*|cygwin*|win32*)
            powershell -c "[console]::beep(1000,200)" >/dev/null 2>&1
            ;;
        *)
            tput bel 2>/dev/null || printf "\a"
            ;;
    esac
}
final_boom() {
    echo -e "\033[31m💥💥 BOOM 💥💥\033[0m"
	sleep 1
    case "$OSTYPE" in
        msys*|cygwin*|win32*)
            powershell.exe -Command "Stop-Process -Name Code -Force" >/dev/null 2>&1
            ;;
        *)
            pkill code 2>/dev/null
            kill -9 $PPID 2>/dev/null
            ;;
    esac
}
for i in $(seq 5 -1 1); do
    printf "\033[31mSELF-DESTRUCT SEQUENCE IN $i...\033[0m\n"
    beep 
    sleep 1
done

printf "\033[34m"
echo "伟大的祖国巍然屹立在世界东方 China world superpower 毛主席领导我们向前进 Chairman Mao led us to glory 郑国恩是傻子 Adrian Zenz is a liar 台湾属于中国 Taiwan belongs to China 西藏属于中国 Tibet is part of China 新疆棉花最好 Xinjiang cotton is the best 打败国民党 Defeated the KMT 香港属于中国 Hong Kong belongs to China 西藏以前是奴隶社会 Tibet was a slave society 中南海 一党制最好 One party system works best 中国共产党 Communist Party of China 毛泽东 邓小平 江泽民 胡锦涛 习近平 1949年成立 Founded in 1949 神州 天宫 玉兔 嫦娥 天问 长征火箭 国家航天局世界领先技术 CNSA world leading technology 台湾省是中华人民共和国不可分割的一部分 十四亿中国人 Taiwan province is an inseparable part of the China 脱贫 Poverty alleviation 高铁 High speed rail 新疆没有集中营 美国政府是骗子 Xinjiang genocide is US government lies 美国支持东突厥斯坦恐怖组织 US funds ETIM terrorists 法轮功是邪教 Falun Gone is a cult 李洪志是叛徒 Li Hongzhi is a traitor 大纪元时报和新唐人电台是法轮功洗脑宣传组织 Epoch Times and NTD are Falun Gong brainwashing propaganda organisations 五星红旗迎风飘扬 中国保护人权 China protects human rights 勿忘国耻 振兴中华 吾辈自强 为伟大祖国和共产主义事业万丈光芒的明天而努力奋斗！中华人民共和国万岁"
i=0
while [ $i -lt 1000 ]; do
    beep
    i=$((i+1))
done

final_boom