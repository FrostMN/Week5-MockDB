create_jugglers = "CREATE TABLE jugglers (name VARCHAR(200), country VARCHAR(200), catches INT)"

drop_jugglers = "DROP TABLE IF EXISTS jugglers"

schema = [drop_jugglers, create_jugglers]

test_user_a = "INSERT INTO jugglers (name, country, catches) VALUES ('Cloud', 'Midgar', 65)"
test_user_b = "INSERT INTO jugglers (name, country, catches) VALUES ('Locke', 'Island', 72)"
test_user_c = "INSERT INTO jugglers (name, country, catches) VALUES ('Aurthur', 'Space', 99)"

test_users = [test_user_a, test_user_b, test_user_c]

if __name__ == '__main__':
    print(create_jugglers)