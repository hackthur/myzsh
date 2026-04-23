                Usuarios / Web / Mobile
                         |
                    API Gateway
                         |
   ---------------------------------------------------------
   |        |         |        |        |        |         |
 Identity  Catalog  Inventory  Cart   Orders   Payments  Notifications
   |         |         |        |        |         |          |
   |         |         |        |        |         |          |
  DB       DB/Cache    DB      Redis     DB        DB         -
                         \        |        /
                          \       |       /
                           ---- Kafka ----
                                  |
                               Search
                                  |
                           Elasticsearch
