from django.core.management.base import BaseCommand
from classical_literature.models import Poetry, Prose
import pinyin

def get_video_path(title, content_type):
    """根据标题生成视频路径"""
    if not title:
        return ""
    
    # 获取标题首字的拼音
    first_char = title[0]
    first_char_pinyin = pinyin.get(first_char, format="strip", delimiter="")
    
    # 构建视频URL
    type_folder = 'poetry' if content_type == 'poetry' else 'prose'
    return f"/classical_literature/static/videos/{type_folder}/{first_char_pinyin}.mp4"

class Command(BaseCommand):
    help = '向数据库中加载古典文学示例数据'

    def handle(self, *args, **kwargs):
        self.stdout.write('开始加载示例数据...')
        
        # 清空现有数据
        Poetry.objects.all().delete()
        Prose.objects.all().delete()
        
        # 添加古诗示例数据
        self.stdout.write('添加古诗数据...')
        poetry_data = [
            {
                'title': '次北固山下',
                'author': '王湾',
                'dynasty': '唐代',
                'content': '客路青山外，行舟绿水前。潮平两岸阔，风正一帆悬。\n海日生残夜，江春入旧年。乡书何处达？归雁洛阳边。',
                'translation': '远方的客路在青山的那边，行船在绿水的前面。涨潮时两岸空阔无边，顺风时船帆高悬。旭日从海上升起，冬去春来又一年。家乡的书信不知寄向何处？只能托付给飞往洛阳的大雁。',
                'type': 'poetry',
                'video_url': get_video_path('次北固山下', 'poetry'),
                'cover_image': '/images/poetry/ci_back1.png'
            },
            {
                'title': '使至塞上',
                'author': '王维',
                'dynasty': '唐代',
                'content': '单车欲问边，属国过居延。征蓬出汉塞，归雁入胡天。\n大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。',
                'translation': '我单独乘坐车子要去边塞访问，途经属国而后到达居延。风吹蓬草出了汉朝的边塞，归雁飞入了北方的天空。广阔的沙漠中一缕孤烟直上，长河落日是那么的圆。在萧关遇到了在边疆守卫的骑兵，都护远在燕然山。',
                'type': 'poetry',
                'video_url': get_video_path('使至塞上', 'poetry'),
                'cover_image': '/images/poetry/shi_back1.png'
            },
            {
                'title': '望岳',
                'author': '杜甫',
                'dynasty': '唐代',
                'content': '岱宗夫如何？齐鲁青未了。造化钟神秀，阴阳割昏晓。\n荡胸生曾云，决眦入归鸟。会当凌绝顶，一览众山小。',
                'translation': '泰山啊你究竟是怎样的？在齐鲁大地上，青色连绵不断。大自然的神奇造化，钟灵毓秀在此一山，它就像是划分了阴阳的分界线。心胸开阔像山中升腾的云雾，目光如炬随归巢飞鸟飞翔。终有一天我要登上泰山之巅，俯瞰群山的渺小。',
                'type': 'poetry',
                'video_url': get_video_path('望岳', 'poetry'),
                'cover_image': '/images/poetry/wang_back1.png'
            },
        ]
        
        for data in poetry_data:
            Poetry.objects.create(**data)
            self.stdout.write(f'已添加古诗：{data["title"]}，视频路径：{data["video_url"]}')
        
        # 添加古文示例数据
        self.stdout.write('添加古文数据...')
        prose_data = [
            {
                'title': '小石潭记',
                'author': '柳宗元',
                'dynasty': '唐代',
                'content': '从小丘西行百二十步，隔篁竹，闻水声，如鸣佩环，心乐之。伐竹取道，下见小潭，水尤清冽。全石以为底，近岸，卷石底以出，为坻，为屿，为嵁，为岩。青树翠蔓，蒙络摇缀，参差披拂。',
                'translation': '从小山丘向西走一百二十步，穿过竹林，听到水声，像佩戴的玉环发出的叮当声，心里感到很愉快。砍伐竹子开出一条路，往下看见一个小潭，水格外清澈冰冷。整个水潭以石头作为底部，靠近岸边的地方，卷曲的石底露出水面，形成矮堤，小岛，突起的石块和岩石。青翠的树木和藤蔓，笼罩缠绕摇曳婆娑，高低错落随风飘拂。',
                'annotation': [
                    {'original': '篁竹', 'explanation': '指竹林'},
                    {'original': '鸣佩环', 'explanation': '形容水声清脆悦耳，如同玉佩相互撞击的声音'},
                    {'original': '坻', 'explanation': '水中的小块陆地'},
                    {'original': '屿', 'explanation': '水中的小岛'},
                    {'original': '嵁', 'explanation': '水中突起的石块'},
                    {'original': '蒙络摇缀', 'explanation': '形容树木藤蔓互相缠绕摇曳的样子'}
                ],
                'appreciation': '《小石潭记》是唐代文学家柳宗元的一篇山水游记，描写了作者被贬永州时游览小石潭的所见所感。文章语言优美，景色描写细腻生动，通过描写小石潭的清幽景色，表达了作者对大自然的热爱和对自由的向往，也流露出被贬后的孤独和忧愁。',
                'type': 'prose',
                'video_url': get_video_path('小石潭记', 'prose'),
                'cover_image': '/images/prose/xiao_back1.png'
            }
        ]
        
        for data in prose_data:
            Prose.objects.create(**data)
            self.stdout.write(f'已添加古文：{data["title"]}，视频路径：{data["video_url"]}')
            
        self.stdout.write(self.style.SUCCESS('示例数据加载完成！')) 