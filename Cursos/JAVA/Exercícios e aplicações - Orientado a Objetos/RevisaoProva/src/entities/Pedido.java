package entities;

import java.util.ArrayList;

interface Pedido {
    void addProduto(PedidoJogo produto);
    ArrayList<PedidoJogo> getProdutos();
    double calculaValorTotal();
}
