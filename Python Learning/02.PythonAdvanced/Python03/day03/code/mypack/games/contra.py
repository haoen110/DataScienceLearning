# mypack/games/contra.py


def play():
    print("正在玩contra")

print('contra 模块被加载')

def gameover():
    # 用绝对路径导入
    # from mypack.menu import show_menu
    # 用相对导入
    from ..menu import show_menu
    show_menu()

    # 绝对导入
    # from mypack.games.tanks import play
    # 相对导入
    # from .tanks import play
    from ..games.tanks import play

    # from ...mypack.games.tanks import play 出错...超出了包的外部
    play()
