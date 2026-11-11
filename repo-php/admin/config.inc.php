<?php
    $conexao = mysqli_connect("db2", "app2user", "app2senha123", "tem_quase_tudo_db");

    if ($conexao){
        echo 'Conexão com banco de dados realizada com sucesso!';
    }else{
        echo "Conexão com banco de dados falhou!";
    }