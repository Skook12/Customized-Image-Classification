# DOCS

Resumo de transfer learning:
Transfer learning é uma abordagem de aprendizado de máquina onde um modelo pré-treinado para uma tarefa é reutilizado em outra tarefa. Esta definição, fornecida por Alexander S. Gillis, Technical Writer and Editor da empresa TechTarget, destaca a popularidade do transfer learning em deep learning. Utilizar um modelo pré-treinado como ponto de partida reduz tanto os recursos computacionais quanto o tempo necessários para o treinamento.
O "Handbook of Research on Machine Learning Applications and Trends: Algorithms, Methods, and Techniques" menciona que o transfer learning melhora a aprendizagem em uma nova tarefa transferindo conhecimento de uma tarefa relacionada já aprendida. Esse conceito é de grande interesse na comunidade de aprendizado de máquina, e a pesquisa atual fornece uma visão geral do estado da arte, abordando tanto o aprendizado indutivo quanto o aprendizado por reforço, e discutindo questões como transferência negativa e mapeamento de tarefas.
Em relação às vantagens, o transfer learning oferece uma maneira eficiente de utilizar modelos pré-treinados, economizando recursos computacionais e tempo, especialmente em tarefas com dados limitados. No entanto, é importante considerar as desvantagens. Dependendo da diferença entre as tarefas pré-treinadas e as novas tarefas, pode ocorrer uma degradação no desempenho do modelo, conhecida como transferência negativa. Além disso, o modelo pré-treinado pode introduzir vieses do conjunto de dados original na nova tarefa, exigindo ajustes adicionais.

Como poderia ter aplicado transfer learning no meu projeto:
No projeto de identificação de imagens, utilizamos um modelo pré-treinado do YOLO para detectar objetos, mas ele não veio treinado especificamente para nossa tarefa. Isso nos fez ter que treinar o modelo com dados, o que demandou tempo. Isso teria sido um lugar onde poderíamos ter aplicado o transfer learning para evitar esse transtorno de ter que treinar o modelo. O YOLO é poderoso para detecção de objetos, mas para identificar objetos específicos em nossas imagens, é crucial treiná-lo com dados relevantes para nossa aplicação ou encontrar um modelo pré-treinado que já consiga fazer isso sem necessitar de muito treinamento. Uma maneira de melhorar o trabalho seria usar alguns desses modelos pré-treinados e ajustá-los para nossa tarefa de identificação de objetos, aproveitando o conhecimento prévio incorporado nesses modelos.


Referências:

GILLIS, A. S.; COLE, B. What is transfer learning? Disponível em: <https://www.techtarget.com/searchcio/definition/transfer-learning>. Acesso em: 15 abr. 2024.
OLIVAS, E. S. et al. Handbook of research on machine learning applications and trends: Algorithms, methods, and techniques. (E. S. Olivas et al., Eds.)IGI Global, , 1 jan. 2010. Disponível em: <https://www.igi-global.com/book/handbook-research-machine-learning-applications/486>. Acesso em: 15 abr. 2024



