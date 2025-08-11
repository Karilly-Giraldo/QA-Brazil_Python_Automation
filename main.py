import data
import helpers

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Adicionar em S8
        print("Verifica preenchimento correto dos campos de endereço.")
        assert True  # Placeholder para futura lógica

    def test_select_plan(self):
        # Adicionar em S8
        print("Função criada para definir a seleção de plano.")
        assert True

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Função criada para definir o número de telefone.")
        assert True

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para definir o número do cartão.")
        assert True

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para definir o comentário ao motorista.")
        assert True

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para definir pedidos de cobertores e lenços.")
        assert True

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            print(f"Função criada para definir o pedido de sorvete número {count + 1}.")
        assert True

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função criada para verificar os modelos de carro que aparecem.")
        assert True