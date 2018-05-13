

# 3.3  Solução do sistema 2RElectronic

  O sistema de eletrônica ficou responsável pelo sensoriamento, aquisição de sinais, tratamentos dos sinais e controle do acionamento das cargas. Os sinais obtidos foram das IMUs e dos botões, este último define qual a carga que deverá ser acionada. Este relatório apresenta a evolução do grupo, assim como as alterações realizadas no escopo do ponto de controle 1.

## 3.3.1 2RE-Suit

  Esse subsistema continha o 2RE-Cardio e o 2RE-IMU. Devido a demanda e necessidade do projeto o 2RE-Cardio teve de ser retirado, a aquisição desse dado não apresenta um parâmetro significativo para o equipamento de remo ergométrico 2Row. Abaixo, serão descritas as soluções, decisões embasadas e testes desse subsistema. 

### 2RE-Cardio: 
  Esse subsistema foi retirado, pois a aquisição dos dados de batimentos cardíacos e a filtragem desses dados requer uma dificuldade que não contempla o tempo estipulado para finalizar o projeto, já que a eletrônica precisa obter e repassar parâmetros que são essenciais para a integração. 

### 2RE-IMU:

  A Unidade de Medida Inercial (IMU) é um sistema microeletromecânico (MEM), que permite identificar a posição  ou o deslocamento de um corpo rígido em um espaço tridimensional. Neste trabalho, a IMU será responsável em determinar a posição do membro inferior direito para a criação de exoesqueleto autónomo para a identificação e correção da postura do praticante de remo indoor. Desse modo, este trabalho sugere implementar uma IMU em dois centros de gravidades, pois nesses pontos a massa está distribuída de forma uniforme,  localizados no membro inferior do exoesqueleto como pode ser visto na Figura {#fig:exoesqueleto}, para estimar a orientação desses pontos onde há equilíbrio de forças (VAUGHAN et al., 1999).
  
  
  ![Celula_s^[Fonte:Adaptado de (VAUGHAN et al., 1999)]](imagens/exoesqueleto.png){#fig:exoesqueleto}
  
  A IMU é composta de três sensores principais, os quais são acelerômetro, giroscópio e magnetômetro, o que possibilita obter continuamente  a variação de velocidade, posição e direção de um corpo rígido (ARAÚJO et al., 2013). Esses sensores podem realizar medições nos eixos de referência x,y e z. A Tabela 1.0 apresenta uma comparação entre IMUs de baixo custo e parâmetros relevantes para a escolha da tecnologia, como: quantidade de sensores embarcados, graus de liberdade, custo.

Tabela 1.0 Tabela de comparação de parâmetros das IMUs de baixo custo.

| Parâmetros            | MPU6050 | MPU9250 | GY80 |
|--------------------   |------------|-------|------------|
| Sensor embarcado      |   Único sensor   |    Único sensor   |      Único sensor    |
| Acelerômetro          |   MPU6050        |   MPU9250 |    ADXL345       |
| Giroscópio            |   MPU6050        |    MPU9250   |     L3G4200D       |
| Magnetômetro          |      -   |    AK8963  |   HMC5883L        |
| Graus de liberdade    |      6   |   9    |     10       |
| Custo                 |   R$ 13,90   |   R$ 25,00    |       R$ 80,00     |


  Em observância com a Tabela 1.0, a IMU selecionada como solução foi a MPU9250, pois a mesma possui um custo baixo e magnetômetro, contemplando 9 graus de liberdade, três graus de liberdade a mais do que a MPU6050. A GY80 possui um custo mais alto comparado aos demais. A Figura 2.0 apresenta a orientação dos eixos dos sensores (a) acelerômetro, (b) giroscópio e (c) magnetômetro, esses dados são essenciais para realização do código para aquisição dos sinais (INVENSENSE, 2016). A Tabela 2.0 apresenta as características do MPU9250. Os três sensores imbutidos na MPU9250 podem obter sinais nos três eixos (x, y, z) e possuem três conversores analógico-digitais (ADCs) de 16 bits, para cada respectivo sensor.
  
![Celula_s^[Fonte:Adaptado de (INVENSENSE, 2016).]](imagens/orientacoes.png){#fig:orientacoes}
 
 
 Tabela 2.0 Características da IMU MPU9250
 
| Características             | MPU9250            |
|------------------------------|--------------------|
| Alimentação                  |       2,4 - 3,6 V  | 
| Dimensão                     |  15 x 25 mm        |    
| Graus de liberdade           |       9            |    
| Interface de comunicação     |     I2C           |   
| Corrente de operação normal  |        3,5 mA   |  
| Frequência de operação       |        400 kHz   |  

Essa corrente de operação é com o DPM habilitado. O DPM é o processador utilizado na IMU9250.

Fonte: (INVENSENSE, 2016)



 
 Foi realizado um código para calibrar as IMUs utilizadas, pois como as medidas devem ser enviadas de forma contínua, é necessário que haja uma maior precisão. 

#### Calibração

Figura 3
Figura 4
Figura 5
Figura 6

#### Protocolo de comunicação I2C

  O protocolo I2C (Inter- Intergrated Circuit) é um barramento de comunicação serial que utiliza dois fios( Serial Data- DAS e Serial Clock- SCL), ou seja sinal de dados e de clock. Ele realiza a comunicação de escrita (W) e leitura (R) entre dois ou mais dispositivos, em que se pode ocorrer entre um mestre e um ou mais escravos. Para que o mestre envie sinal para determinado escravo ele precisa saber qual o endereço do escravo. Cada escravo tem um endereço específico de identificação, composto de 7 bits. Neste trabalho, o dispositivo dimensionado como mestre é o microcontrolador ESP8366 Node-MCU, e o escravo é a MPU9250. Tem-se também o escravo do escravo, o qual é o segundo MPU9250. ço do escravo a ser contactado.
  
   A Figura X apresenta um exemplo do protocolo de comunicação I2C. A comunicação é iniciada pelo mestre, o início e término da comunicação é determinada pela variação do clock do nível baixo para alto. Por outro lado, para que aconteça o envio de dados o SDA tem de mudar de nível lógico quando o SCL estiver em nível baixo, depois de ter ocorrido a transição desse, de alto para baixo (critério de início) e de baixo para alto (critério de término). Feito isso, o mestre envia 1 byte, em que o bit menos significativo representa a seleção de escrita (‘1’) ou leitura (‘0’) e os demais bits representam o endereço do escravo que ele quer se comunicar. O escravo por sua vez retorna um sinal, Acknowledge (ACK), em que nível baixo indica que ele está pronto para aceitar os dados e nível alto indica um sinal de não reconhecimento,  Not Acknowledge  (NACK). Depois da validação de reconhecimento ocorre a troca de dados pelo pino SDA, até que a condição de término seja satisfeita.
  
   Figura 7 do protocolo
  
  Ao colocar o segundo MPU9250, segundo escravo, para que não houvesse curto-circuito nas linhas de transmissão foram colocadas resistências de pull-up de (valor das resistências) 
  
  
  
  Explicação do código de leitura Multiplexação com base nos registradores.
   Explicação da Esp8266
   Explicação do cálculo de sensibilidade e tem de colocá-lo aqui.
   Envio de dados via MQTT 
   Explicação do código
   Cálculo da taxa de transmissão de dados





