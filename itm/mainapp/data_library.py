import pymysql
from itm import settings
import pymysqlite
from datetime import datetime as dt


def get_orders_filter(filter_data=None):
    conn = pymysqlite.connect(database=settings.DATABASES.get('default').get('NAME'))
    custom_filter = ''
    if filter_data:
        custom_filter += 'WHERE'
        for key, val in filter_data.items():
            if len(custom_filter) > 10:
                if key == 'pay_status':
                    custom_filter += f''' AND `pay_date` '''
                elif key == 'author':
                    custom_filter += f''' AND `author`={val} '''
                else:
                    custom_filter += f''' AND `b`.`{key}` = '{val}' '''
            else:
                if key == 'pay_status':
                    custom_filter += f''' `pay_date` '''
                elif key == 'author':
                    custom_filter += f''' `author`={val} '''
                else:
                    custom_filter += f''' `b`.`{key}`='{val}' '''

    try:
        with conn.cursor() as cursor:
            response = f'''
            SELECT
                `b`.`id`,
                (SELECT `cu`.`username` FROM authapp_customuser cu 
                WHERE `cu`.`id`=(SELECT `s`.`custom_user_id_id` FROM mainapp_services s WHERE `b`.`service_id_id`=`s`.`id`)) as author,
                (SELECT `cu`.`username` FROM authapp_customuser cu WHERE `b`.`custom_user_id_id`=`cu`.`id`) as custom_user_id,
                (SELECT `s`.`name` FROM mainapp_services s WHERE `b`.`service_id_id`=`s`.`id`) as service_id,
                `b`.`create_date`,
                `b`.`pay_date`,
                `b`.`status_completed`
            FROM `mainapp_basket` b
            {custom_filter}
            '''
            cursor.execute(response)
            response = cursor.fetchall()
    finally:
        conn.close()
    return response
