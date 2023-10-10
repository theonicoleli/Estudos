<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estudos de PHP</title>
</head>
<body>
    <?php
        // Criação de variaveis
        $testVar = true;

        // Funções
        function somar($valorA, $valorB) {
            return $valorA + $valorB;
        }

        // if e else
        if ($testVar) {
            echo "testVar é : $testVar<br>";
            echo somar(10, 5) . "<br>";
        } else {
            echo "testVar é falso, portanto ele não realiza soma.<br>";
        }

        // for
        for ($i = 0; $i<10; $i++) {
            echo "Olá!<br>";
        }

        // While
        $i = 0;
        while ($i < 2) {
            echo "Entrei no while!<br>";
            $i++;
        }

        echo "<br><br>";
    ?>

    <?php
        //CRIANDO FORMULÁRIO GET
        $nome = isset($_GET["nome"]) ? $_GET["nome"] : "";
        $email = isset($_GET["email"]) ? $_GET["email"] : "";

        echo "Nome: $nome <br>";
        echo "Nome: $email <br>";
    ?>
    <form method="get">
        Nome: <input type="text" name="nome"
            value="<?=$nome?>"><br><br>
        Email: <input type="text" name="email"
            value="<?=$email?>"><br><br>
        <input type="submit" name="submit" value="Enviar">
    </form>

    <?php
        //CRIANDO FORMULÁRIO POST
        $nome = isset($_POST["nome"]) ? $_POST["nome"] : "";
        $email = isset($_POST["email"]) ? $_POST["email"] : "";

        echo "Nome: $nome <br>";
        echo "Nome: $email <br>";
    ?>
    <form method="post">
        Nome: <input type="text" name="nome"
            value="<?=$nome?>"><br><br>
        Email: <input type="text" name="email"
            value="<?=$email?>"><br><br>
        <input type="submit" name="submit" value="Enviar">
    </form>
</body>
</html>