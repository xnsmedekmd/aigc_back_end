from django.core.management.base import BaseCommand
from classical_literature.models import Poetry, Prose

class Command(BaseCommand):
    help = '填充古典文学数据到数据库'

    def handle(self, *args, **kwargs):
        # 清空现有数据
        Poetry.objects.all().delete()
        Prose.objects.all().delete()
        
        # 创建古诗数据
        poetry_data = [
            {
                "id": 1,
                "title": "次北固山下",
                "author": "王湾",
                "dynasty": "唐代",
                "content": "客路青山外，行舟绿水前。潮平两岸阔，风正一帆悬。\n海日生残夜，江春入旧年。乡书何处达？归雁洛阳边。",
                "translation": "郁郁葱葱的山外是旅客的道路，船航行在绿水之间。潮水涨满，两岸与江水齐平，整个江面十分开阔，帆顺着风端直高挂。夜幕还没有褪尽，旭日已在江上冉冉升起，江上春早，旧年未过新春已来。我的家书应该送到什么地方呢？北去的归雁啊，请给我捎回洛阳那边！",
                "type": "poetry",
                "video_url": "/classical_literature/static/videos/ci.mp4",
                "cover_image": "/classical_literature/static/images/ci_back1.png"
            },
            {
                "id": 2,
                "title": "使至塞上",
                "author": "王维",
                "dynasty": "唐代",
                "content": "单车欲问边，属国过居延。征蓬出汉塞，归雁入胡天。\n大漠孤烟直，长河落日圆。萧关逢候骑，都护在燕然。",
                "translation": "轻车简从将要去慰问边关，我要到远在西北边塞的居延。像随风而去的蓬草一样出临边塞，北归大雁正翱翔云天。浩瀚沙漠中孤烟直上云霄，黄河边上落日浑圆。到萧关时遇到侦察骑兵，得知主帅尚在前线未归。",
                "type": "poetry",
                "video_url": "/classical_literature/static/videos/shi.mp4",
                "cover_image": "/classical_literature/static/images/shi_back1.png"
            },
            {
                "id": 3,
                "title": "望岳",
                "author": "杜甫",
                "dynasty": "唐代",
                "content": "岱宗夫如何？齐鲁青未了。造化钟神秀，阴阳割昏晓。\n荡胸生曾云，决眦入归鸟。会当凌绝顶，一览众山小。",
                "translation": "五岳之首的泰山怎么样？在齐鲁大地上，那苍翠的美好山色没有尽头。大自然把神奇秀丽的景象全都汇聚其中，山南山北阴阳分界，晨昏迥然不同。升腾的层层云气，使心胸摇荡；极力张大眼睛远望归鸟隐入了山林。我定要登上那最高峰，俯瞰在泰山面前显得渺小的群山。",
                "type": "poetry",
                "video_url": "/classical_literature/static/videos/wang.mp4",
                "cover_image": "/classical_literature/static/images/wang_back1.png"
            }
        ]
        
        # 创建古文数据
        prose_data = [
            {
                "id": 1,
                "title": "小石潭记",
                "author": "柳宗元",
                "dynasty": "唐代",
                "content": "从小丘西行百二十步，隔篁竹，闻水声，如鸣珮环，心乐之。伐竹取道，下见小潭，水尤清冽。全石以为底，近岸，卷石底以出，为坻，为屿，为嵁，为岩。青树翠蔓，蒙络摇缀，参差披拂。潭中鱼可百许头，皆若空游无所依。日光下澈，影布石上，佁然不动，俶尔远逝，往来翕忽。似与游者相乐。潭西南而望，斗折蛇行，明灭可见。其岸势犬牙差互，不可知其源。坐潭上，四面竹树环合，寂寥无人，凄神寒骨，悄怆幽邃。以其境过清，不可久居，乃记之而去。同游者：吴武陵，龚古，余弟宗玄。隶而从者，崔氏二小生：曰恕己，曰奉壹。",
                "translation": "从小土丘往西走约一百二十步，隔着竹林，听到水声，好象挂在身上的玉佩、玉环相互碰撞的声音，心里很是高兴。（于是）砍伐竹子，开出一条道路，下面显现出一个小小的水潭，潭水特别清凉。潭以整块石头为底，靠近岸边，石底向上弯曲，露出水面，像各种各样的石头和小岛。青葱的树木，翠绿的藤蔓，遮掩缠绕，摇动下垂，参差不齐，随风飘动。　潭中大约有一百来条鱼，都好像在空中游动，没有什么依靠似的。阳光往下一直照到潭底，鱼儿的影子映在水底的石上。（鱼儿）呆呆地静止不动，忽然间（又）向远处游去，来来往往，轻快敏捷，好像跟游人逗乐似的　　向石潭的西南方向望去，（溪流）像北斗七星那样的曲折，（又）像蛇爬行一样的蜿蜒，（有时）看得见，（有时）看不见。两岸的形状像犬牙似的参差不齐，看不出溪水的源头在哪里。　　坐在石潭旁边，四面被竹林树木包围着，静悄悄的，空无一人，（这气氛）使人感到心神凄凉，寒气透骨，幽静深远，弥漫着忧伤的气息。因为环境过于凄清，不能长时间地待下去，就记下这番景致离开了。　　一同去游览的有吴武陵、龚古和我的弟弟宗玄。跟着一同去的还有姓崔的两个年轻人，一个叫恕己，一个叫奉壹。",
                "type": "prose",
                "video_url": "/classical_literature/static/videos/xiao.mp4",
                "cover_image": "/classical_literature/static/images/xiao_back1.png",
                "annotation": [
                    {"original": "篁竹", "explanation": "指竹林"},
                    {"original": "鸣佩环", "explanation": "形容水声清脆悦耳，如同玉佩相互撞击的声音"},
                    {"original": "坻", "explanation": "水中的小块陆地"},
                    {"original": "屿", "explanation": "水中的小岛"},
                    {"original": "嵁", "explanation": "水中突起的石块"},
                    {"original": "蒙络摇缀", "explanation": "形容树木藤蔓互相缠绕摇曳的样子"}
                ],
                "appreciation": "《小石潭记》是唐代文学家柳宗元的一篇山水游记，描写了作者被贬永州时游览小石潭的所见所感。文章语言优美，景色描写细腻生动，通过描写小石潭的清幽景色，表达了作者对大自然的热爱和对自由的向往，也流露出被贬后的孤独和忧愁。"
            }
        ]

        # 批量创建数据
        for data in poetry_data:
            Poetry.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'成功创建古诗：{data["title"]}'))

        for data in prose_data:
            Prose.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'成功创建古文：{data["title"]}'))

        self.stdout.write(self.style.SUCCESS('数据填充完成')) 