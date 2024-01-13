import mysql.connector
from mysql.connector import Error

# データベースの作成
try:
    # MySQLデータベースサーバーに接続
    connection = mysql.connector.connect(
        host='127.0.0.1',        # ホスト名またはIPアドレス
        user='root',    # MySQLのユーザー名
        password='root' # ユーザーのパスワード
    )

    if connection.is_connected():
        # データベースを作成するためのカーソルを作成
        cursor = connection.cursor()
        # データベースを作成するSQLコマンド
        cursor.execute("CREATE DATABASE IF NOT EXISTS main_db")
        print("Database is created")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# テーブルの作成
try:
    # 新しく作成したデータベースに接続
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        database='main_db',
        user='root',
        password='root'
    )

    if connection.is_connected():
        # テーブルを作成するためのカーソルを作成
        cursor = connection.cursor()
        
        # テーブルを作成するSQLコマンド
        create_table_query = """
        CREATE TABLE IF NOT EXISTS games (
            id VARCHAR(255) PRIMARY KEY,
            date DATE,
            day_week VARCHAR(255),
            stadium VARCHAR(255),
            first_team_id INT,
            second_team_id INT,
            first_hits INT,
            second_hits INT,
            first_miss INT,
            second_miss INT,
            first_point_1 INT,
            first_point_2 INT,
            first_point_3 INT,
            first_point_4 INT,
            first_point_5 INT,
            first_point_6 INT,
            first_point_7 INT,
            first_point_8 INT,
            first_point_9 INT,
            first_point10 INT,
            first_point11 INT,
            first_point12 INT,
            first_point_total INT,
            second_point_1 INT,
            second_point_2 INT,
            second_point_3 INT,
            second_point_4 INT,
            second_point_5 INT,
            second_point_6 INT,
            second_point_7 INT,
            second_point_8 INT,
            second_point_9 INT,
            second_point10 INT,
            second_point11 INT,
            second_point12 INT,
            second_point_total INT
        )
        """
        cursor.execute(create_table_query)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS fielder_results (
            uuid INT PRIMARY KEY,
            player_id VARCHAR(255),
            game_id VARCHAR(255),
            times_at_bat INT,
            run INT,
            hits INT,
            rbi INT,
            k INT,
            walks INT,
            hit_by_pitch INT,
            sacrifice INT,
            steal INT,
            miss INT,
            hr INT
        )
        """
        cursor.execute(create_table_query)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS pitcher_results (
            uuid INT PRIMARY KEY,
            player_id VARCHAR(255),
            game_id VARCHAR(255),
            inning FLOAT,
            pitch_num INT,
            batter_match_num INT,
            hits INT,
            hr INT,
            k INT,
            walks INT,
            hit_by_pitch INT,
            balks INT,
            run INT,
            er INT
        )
        """
        cursor.execute(create_table_query)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS bats
            id INT PRIMARY KEY,
            game_id VARCHAR(255),
            inning INT,
            attack_team_id INT,
            defend_team_id INT,
            is_on_base BOOLEAN,
            rbi INT
        """

        create_table_query = """
        CREATE TABLE IF NOT EXISTS pitch_stats (
            uuid INT PRIMARY KEY,
            id_at_bat INT,
            pitcher_id INT,
            is_pitcher_left BOOLEAN,
            batter_id INT,
            is_batter_left BOOLEAN,
            in_box_count INT,
            match_count INT,
            c_id INT,
            first_id INT,
            second_id INT,
            third_id INT,
            ss_id INT,
            lf_id INT,
            cf_id INT,
            rf_id INT,
            first_runner_id INT,
            second_runner_id INT,
            third_runner_id INT,
            ball_type VARCHAR(255),
            speed int,
            pitch_count_at_bat INT,
            pitch_count_at_game INT,
            ball_result VARCHAR(255),
            strike_count INT,
            ball_count INT,
            top_coordinate INT,
            left_coordinate INT,
            result_big VARCHAR(255),
            result_small VARCHAR(255),
            steal BOOLEAN
        )
        """
        cursor.execute(create_table_query)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS players (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            team_id INT,
            uniform_number INT,
            position VARCHAR(255),
            height INT,
            weight INT,
            throw_arm VARCHAR(255),
            bat_arm VARCHAR(255),
            draft_year INT,
            draft_rank INT,
            total_years INT
        )
        """
        cursor.execute(create_table_query)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS teams (
            id INT PRIMARY KEY,
            name VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)

        print("Table is created")

except Error as e:
    print("Error while connecting to MySQL", e)



finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
