<?php
    //apiキー
    $API_KEY = "入手したAPIキー";
    if(isset($_POST["name"])){
        //サモナーネーム取得
        $name = rawurlencode($_POST['name']);
        //リージョン取得
        $region = $_POST['region'];
        //url
        $url = "https://${region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/${name}?api_key=${API_KEY}";
        //サモナー情報取得
        $array = json_decode(file_get_contents($url),true);
    }
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>サモナーネーム検索</title>
    </head>
    <body>
        <form action="" method="POST">
            <p>サモナーネームを入力してください</p>
            <input type="text" name="name" placeholder="例:RuRey 0w0">
            <select name="region">
                <option value=""></option>
                <option value="na1">NA</option>
                <option value="kr">KR</option>
                <option value="jp1">JP</option>
            </select>
            <input type="submit" value="送信">
        </form>
        <div>
            <?php
                //出力
                foreach($array as $key => $value){
                    //名前とサモナーレベル出力
                    if($key == "name" || $key == "summonerLevel"){
                        echo $key;
                        echo ":";
                        echo $value;
                        echo "<br>";
                    }
                    //ddragonからアイコンの画像を取得
                    if($key == "profileIconId"){
                        print '<image src="http://ddragon.leagueoflegends.com/cdn/9.9.1/img/profileicon/'.$value.'.png" width=100px; heigth=100px;></image>';
                        echo "<br>";
                    }
                }
            ?>
        </div>
    </body>
</html>
