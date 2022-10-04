import redshift_connector
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    try:
        conn = redshift_connector.connect(
            iam=True,
            host='',
            database='dev',
            db_user='awsuser',
            role_arn='',
            cluster_identifier='',
            auto_create=True
        )
        cursor: redshift_connector.Cursor = conn.cursor()
        cursor.execute("select * from pg_user")
        result = cursor.fetchall()
        print(result[0][0])
    except Exception as e:
        print(e)


