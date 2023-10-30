<?php
    echo "Arquivo: " . __FILE__ . "<br>";
    echo "Versão: " . PHP_VERSION . "<br>";
    echo "OS: " . PHP_OS . "<br>";

    $var = 10;

    var_dump(5 > 4 && 5 > 3);

    echo "<br>Variável valor: " . $var ;

    function somar(&$var, &$var2) {
        $var += 10;
        $var2 += 15;

        $newVar = $var + $var2;

        echo "<br> O valor da soma dos novos valores das variaveis é de: $newVar<br>";
    }

    $variavel = 10;
    $variavel2 = 12;

    somar($variavel, $variavel2);

    echo "$variavel e $variavel2";

    $userArray = array("name"=>"José Alencar", "city"=>"Curitiba");

    echo "<br>Nome: " . $userArray["name"] . ", Cidade: " . $userArray["city"];

    $books = array();

    $books[0] = array("name"=>"José Maria", "cidade"=>"Assaí");
    $books[1] = array("name"=>"Maria João", "cidade"=>"Londrina");
    $books[2] = array("name"=>"João José", "cidade"=>"Astorga");

    echo "<br>" . $books[1]["name"];

    for ($i = 0; $i < sizeof($books); $i++) {
        foreach ($books[$i] as $key=>$value) {
            echo "<br>";
            echo "Chave = $key<br>";
            echo "Valor = $value<br>";
        }
    }
?>