# Generated by Django 2.0 on 2018-04-09 20:10

import apps.sspanel.tools
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AliveIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('ip', models.CharField(max_length=128, verbose_name='设备ip')),
                ('user', models.CharField(max_length=128, verbose_name='用户名')),
                ('log_time', models.DateTimeField(auto_now=True, verbose_name='日志时间')),
            ],
            options={
                'verbose_name_plural': '节点在线IP',
                'ordering': ['-log_time'],
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(unique=True, verbose_name='节点id')),
                ('country', models.CharField(choices=[('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia (Plurinational State of)'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CD', 'Congo (the Democratic Republic of the)'), ('CG', 'Congo'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands  [Malvinas]'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran (Islamic Republic of)'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea (the Democratic People's Republic of)"), ('KR', 'Korea (the Republic of)'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova (the Republic of)'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine, State of'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan (Province of China)'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], default='CN', max_length=2, verbose_name='国家')),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('server', models.CharField(max_length=128, verbose_name='服务器IP')),
                ('method', models.CharField(choices=[('aes-256-cfb', 'aes-256-cfb'), ('aes-128-ctr', 'aes-128-ctr'), ('rc4-md5', 'rc4-md5'), ('salsa20', 'salsa20'), ('chacha20', 'chacha20'), ('none', 'none')], default='aes-128-ctr', max_length=32, verbose_name='加密类型')),
                ('custom_method', models.SmallIntegerField(choices=[(0, 0), (1, 1)], default=0, verbose_name='自定义加密')),
                ('traffic_rate', models.FloatField(default=1.0, verbose_name='流量比例')),
                ('protocol', models.CharField(choices=[('auth_sha1_v4', 'auth_sha1_v4'), ('auth_aes128_md5', 'auth_aes128_md5'), ('auth_aes128_sha1', 'auth_aes128_sha1'), ('auth_chain_a', 'auth_chain_a'), ('origin', 'origin')], default='auth_chain_a', max_length=32, verbose_name='协议')),
                ('obfs', models.CharField(choices=[('plain', 'plain'), ('http_simple', 'http_simple'), ('http_simple_compatible', 'http_simple_compatible'), ('http_post', 'http_post'), ('tls1.2_ticket_auth', 'tls1.2_ticket_auth')], default='http_simple', max_length=32, verbose_name='混淆')),
                ('info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='节点说明')),
                ('status', models.CharField(choices=[('好用', '好用'), ('维护', '维护'), ('坏了', '坏了')], default='ok', max_length=32, verbose_name='状态')),
                ('level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)], verbose_name='节点等级')),
                ('show', models.CharField(choices=[('显示', '显示'), ('不显示', '不显示')], default='显示', max_length=32, verbose_name='是否显示')),
                ('group', models.CharField(default='谜之屋', max_length=32, verbose_name='分组名')),
                ('total_traffic', models.BigIntegerField(default=0, verbose_name='总流量')),
                ('human_total_traffic', models.CharField(blank=True, default='1GB', max_length=255, null=True, verbose_name='节点总流量')),
                ('used_traffic', models.BigIntegerField(default=0, verbose_name='已用流量')),
                ('human_used_traffic', models.CharField(blank=True, max_length=255, null=True, verbose_name='已用流量')),
            ],
            options={
                'verbose_name_plural': '节点',
                'db_table': 'ss_node',
                'ordering': ['-show', 'level'],
            },
        ),
        migrations.CreateModel(
            name='NodeInfoLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('uptime', models.FloatField(verbose_name='更新时间')),
                ('load', models.CharField(max_length=32, verbose_name='负载')),
                ('log_time', models.IntegerField(verbose_name='日志时间')),
            ],
            options={
                'verbose_name_plural': '节点日志',
                'db_table': 'ss_node_info_log',
                'ordering': ('-log_time',),
            },
        ),
        migrations.CreateModel(
            name='NodeOnlineLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('online_user', models.IntegerField(verbose_name='在线人数')),
                ('log_time', models.IntegerField(verbose_name='日志时间')),
            ],
            options={
                'verbose_name_plural': '节点在线记录',
                'db_table': 'ss_node_online_log',
            },
        ),
        migrations.CreateModel(
            name='SSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_check_in_time', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 8, 0), editable=False, null=True, verbose_name='最后签到时间')),
                ('password', models.CharField(db_column='passwd', default=apps.sspanel.tools.get_short_random_string, max_length=32, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='sspanel密码')),
                ('port', models.IntegerField(db_column='port', unique=True, verbose_name='端口')),
                ('last_use_time', models.IntegerField(db_column='t', default=0, editable=False, help_text='时间戳', verbose_name='最后使用时间')),
                ('upload_traffic', models.BigIntegerField(db_column='u', default=0, verbose_name='上传流量')),
                ('download_traffic', models.BigIntegerField(db_column='d', default=0, verbose_name='下载流量')),
                ('transfer_enable', models.BigIntegerField(db_column='transfer_enable', default=5368709120, verbose_name='总流量')),
                ('switch', models.BooleanField(db_column='switch', default=True, verbose_name='保留字段switch')),
                ('enable', models.BooleanField(db_column='enable', default=True, verbose_name='开启与否')),
                ('method', models.CharField(choices=[('aes-256-cfb', 'aes-256-cfb'), ('aes-128-ctr', 'aes-128-ctr'), ('rc4-md5', 'rc4-md5'), ('salsa20', 'salsa20'), ('chacha20', 'chacha20'), ('none', 'none')], default='aes-128-ctr', max_length=32, verbose_name='加密类型')),
                ('protocol', models.CharField(choices=[('auth_sha1_v4', 'auth_sha1_v4'), ('auth_aes128_md5', 'auth_aes128_md5'), ('auth_aes128_sha1', 'auth_aes128_sha1'), ('auth_chain_a', 'auth_chain_a'), ('origin', 'origin')], default='auth_chain_a', max_length=32, verbose_name='协议')),
                ('obfs', models.CharField(choices=[('plain', 'plain'), ('http_simple', 'http_simple'), ('http_simple_compatible', 'http_simple_compatible'), ('http_post', 'http_post'), ('tls1.2_ticket_auth', 'tls1.2_ticket_auth')], default='http_simple', max_length=32, verbose_name='混淆')),
                ('level', models.PositiveIntegerField(default=0, verbose_name='用户等级')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ss_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SS账户',
                'db_table': 'user',
                'ordering': ('-last_check_in_time',),
            },
        ),
        migrations.CreateModel(
            name='TrafficLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('upload_traffic', models.BigIntegerField(db_column='u', default=0, verbose_name='上传流量')),
                ('download_traffic', models.BigIntegerField(db_column='d', default=0, verbose_name='下载流量')),
                ('rate', models.FloatField(default=1.0, verbose_name='流量比例')),
                ('traffic', models.CharField(max_length=32, verbose_name='流量记录')),
                ('log_time', models.IntegerField(verbose_name='日志时间')),
                ('log_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='记录日期')),
            ],
            options={
                'verbose_name_plural': '流量记录',
                'db_table': 'user_traffic_log',
                'ordering': ('-log_time',),
            },
        ),
    ]
