### 2RE-Watt

Subsistema inicialmente denominado 2RE-Volt, que a princípio seria responsável por medir a tensão das cargas no gerador para encontrar, sabendo a carga do gerador em atuação, a potência elétrica durante a realização da remada do atleta.
Após testes preliminares a solução de energia decidiu mudar o método de manter uma força contrário ao movimento do atleta e então optou-se pelo freio eletromagnético. Portanto, eletrônica teve que encontrar outra solução para medição da potência mecânica do atleta durante o movimento.


Foram analisadas então 2 opções para medição da potência do movimento: wattímetro no eixo rotativo e células de carga (strain gage) sob os pés do atleta, então foram geradas as tabelas a seguir:

| Compontes do Wattímetro | Quantidade | Média de Preço (R$) | Localização do Fornecedor |
|--------------------------|------------|-------|------------|
| Torquímetro digital                    |        1   |    630,00   |      São Paulo      |
| Encoder                      |        1   |    120,00   |     São Paulo       |
| Wattímetro digital         |        1   |    2.000,00   |     São Paulo       |

**Colocar as imagens de todos os subcomponentes pensados para escolha

![Torquímetro_digital^[Fonte: https://produto.mercadolivre.com.br/MLB-703889366-torquimetro-digital-12-de-4-a-20-kgf-m-waft-_JM]](imagens/torquimetro.png){#fig:torquimetro}

![Encoder^[Fonte: https://produto.mercadolivre.com.br/MLB-882483511-encoder-incremental-rotativo-600-pulsos-eixo-6mm-5-24v--_JM]](imagens/encoder.png){#fig:encoder}

![Wattímetro^[Fonte: https://produto.mercadolivre.com.br/MLB-945963390-medidor-de-potncia-stages-bluetooth-modelo-spm1-175mm-_JM]](imagens/wattimetro.png){#fig:wattimetro}

| Compontes da Célula de Carga | Quantidade | Média de Preço (R$) | Localização do Fornecedor |
|--------------------------|------------|-------|------------|
| Strain gage modelo S                  |        2   |    200,00   |      São Paulo      |
| Strain gage modelo viga de flexão                  |        2   |    130,00   |      São Paulo      |
| HX711         |        2   |    15,00   |     Brasília       |

![Celula_s^[Fonte: ]](imagens/modelo_s.jpeg){#fig:modelo_s}

![Celula_de_carga^[Fonte: https://produto.mercadolivre.com.br/MLB-931359038-celula-de-carga-sensor-de-peso-200kg-200-kg-0296-_JM]](imagens/celula.png){#fig:celula_de_carga}


![HX711^[Fonte: https://produto.mercadolivre.com.br/MLB-930850652-modulo-conversor-hx711-para-sensor-de-peso-projeto-arduino-_JM]](imagens/hx711.png){#fig:hx711}



Portanto, analisando valores e disponibilidade rápida para entrega, concluímos que comprar um wattímetro pronto estaria fora do orçamento do nosso projeto uma vez que seu valor é muito alto, também analisamos comprar um torquímetro e um encoder mas seria uma solução relativamente complexa do ponto de vista de integração e também por aumentar o escopo do projeto, uma vez que já há demasiado trabalho a ser realizado. Por isso optamos por colocar 2 células de carga na base para os pés para realizar medições de força e transformar em potência, como será explicado abaixo. Entre os modelos pesquisados para servir como célula de carga, o modelo S e o modelo de viga de flexão foram os que mais se adaptaram às necessidades do projeto. Pensando na alocação dos sensores no subsistema 2RE-Boat, foi escolhida então a célula de carga modelo S pois a mesma ocuparia menos espaço e tem o limite de força adequado à medição necessária.

Para realizar a medição da força a partir da célula de carga foi necessário utilizar um componente que converte as saídas analógicasa do strain gage em saídas digitais, o componente em questão é o hx711. Para realizar os testes do subsistema realizou-se a leitura na Raspberry Pi 3 em seus pinos GPIO, um programa em python foi criado e a leitura da força pôde ser realizada, o modelo de célula de carga escolhida suporta o limite de 200 kg, passando do limite estabelicido no projeto, no entrando também trabalha em medições de unidades de peso, ou seja, um dos fatores para utilizarmos a mesma foi a disponibilidade de empréstimo de 2 células de carga do modelo S por professores da FGA.


