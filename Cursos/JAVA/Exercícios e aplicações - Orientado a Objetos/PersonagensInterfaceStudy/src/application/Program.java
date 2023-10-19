package application;

import entities.*;

import java.util.ArrayList;

public class Program {
    public static void main(String[] args) {

        ArrayList<Personagem> personagens = new ArrayList<>();

        boolean vivo = true;
        double posicao_x = 37;
        double posicao_y = 345;
        double posicao_z = 10;
        int cor = 1;

        Personagem batman = new Batman(vivo, posicao_x, posicao_y, posicao_z, 1);
        batman.atirar();
        ((Batman) batman).camuflar(cor);

        personagens.add(batman);

        Personagem coringa = new Coringa(vivo, posicao_x, posicao_y, posicao_z, 2);
        coringa.atirar();

        personagens.add(coringa);

        Personagem drno = new Drno(vivo, posicao_x, posicao_y, posicao_z, cor);
        drno.saltar();
        drno.atirar();
        drno.correr();

        personagens.add(drno);

        Personagem goldfinger = new Goldfinger(vivo, posicao_x, posicao_y, posicao_z, cor);
        ((Goldfinger) goldfinger).camuflar(cor);
        ((Goldfinger) goldfinger).personificar((Heroi) batman);

        personagens.add(goldfinger);

        Personagem pinguim = new Pinguim(vivo, posicao_x, posicao_y, posicao_z, cor);
        pinguim.atirar();
        pinguim.correr();

        personagens.add(pinguim);

        Personagem jamesBond = new JamesBond(vivo, posicao_x, posicao_y, posicao_z, cor);
        jamesBond.atirar();
        jamesBond.saltar();

        personagens.add(jamesBond);

        for (Personagem personagem : personagens) {
            personagem.vivoMorto();
        }

        for (Personagem personagem : personagens) {
            personagem.morrer();
            personagem.vivoMorto();
        }

        batman.atirar(); // Não pode atirar, pois está morto!
    }
}
