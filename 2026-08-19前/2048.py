import pygame
import random
import sys

# -------------------------- 界面常量配置 --------------------------
WIDTH = 400
HEIGHT = 500
GRID_SIZE = 4
CELL_SIZE = 80
GAP = 10
MARGIN = (WIDTH - GRID_SIZE * CELL_SIZE - (GRID_SIZE - 1) * GAP) // 2
TOP_MARGIN = 100

# 颜色定义 (R, G, B)
BG_COLOR = (187, 173, 160)
CELL_BG_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
TEXT_COLOR_LIGHT = (249, 246, 242)  # 大数字浅色字
TEXT_COLOR_DARK = (119, 110, 101)  # 小数字深色字
SCORE_COLOR = (255, 255, 255)


# -------------------------- 核心游戏逻辑 --------------------------
def init_grid():
    """初始化4x4网格，生成2个初始方块"""
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid


def add_new_tile(grid):
    """在空白位置随机生成2(90%概率)或4(10%概率)"""
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    grid[i][j] = 2 if random.random() < 0.9 else 4


def move_row_left(row):
    """单行左移+合并逻辑，返回新行和本次合并获得的分数"""
    # 1. 压缩：去掉所有0
    non_zero = [num for num in row if num != 0]
    # 2. 合并：相邻相同数字相加
    merged = []
    score_add = 0
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            val = non_zero[i] * 2
            merged.append(val)
            score_add += val
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1
    # 3. 补零：末尾补0保持长度为4
    merged += [0] * (GRID_SIZE - len(merged))
    return merged, score_add


def move_left(grid):
    """整个网格左移"""
    new_grid = []
    total_add = 0
    for row in grid:
        new_row, add = move_row_left(row)
        new_grid.append(new_row)
        total_add += add
    return new_grid, total_add


def move_right(grid):
    """右移：反转每行 → 左移 → 反转回来（复用左移逻辑）"""
    new_grid = []
    total_add = 0
    for row in grid:
        reversed_row = row[::-1]
        new_row, add = move_row_left(reversed_row)
        new_grid.append(new_row[::-1])
        total_add += add
    return new_grid, total_add


def move_up(grid):
    """上移：矩阵转置（行变列） → 左移 → 转置回来"""
    transposed = [list(col) for col in zip(*grid)]
    moved, total_add = move_left(transposed)
    return [list(col) for col in zip(*moved)], total_add


def move_down(grid):
    """下移：转置 + 反转每行 → 左移 → 反转 + 转置回来"""
    transposed = [list(col) for col in zip(*grid)]
    reversed_grid = [row[::-1] for row in transposed]
    moved, total_add = move_left(reversed_grid)
    reversed_back = [row[::-1] for row in moved]
    return [list(col) for col in zip(*reversed_back)], total_add


def is_grid_changed(old_grid, new_grid):
    """判断移动后网格是否发生变化（无效移动不生成新方块）"""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if old_grid[i][j] != new_grid[i][j]:
                return True
    return False


def is_game_over(grid):
    """判断游戏结束：无空格且无可合并的相邻数字"""
    # 存在空格则未结束
    for row in grid:
        if 0 in row:
            return False
    # 横向检查可合并项
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i][j + 1]:
                return False
    # 纵向检查可合并项
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i + 1][j]:
                return False
    return True


# -------------------------- 界面绘制 --------------------------
def draw_game(screen, grid, score):
    """绘制游戏整体画面"""
    screen.fill(BG_COLOR)

    # 绘制分数
    font = pygame.font.SysFont("arial", 30, bold=True)
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    screen.blit(score_text, (MARGIN, 40))

    # 绘制每个格子与数字
    font = pygame.font.SysFont("arial", 36, bold=True)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            x = MARGIN + j * (CELL_SIZE + GAP)
            y = TOP_MARGIN + i * (CELL_SIZE + GAP)

            # 格子背景
            color = CELL_BG_COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE), border_radius=6)

            # 数字文字（居中）
            if value != 0:
                text_color = TEXT_COLOR_LIGHT if value >= 8 else TEXT_COLOR_DARK
                text_surface = font.render(str(value), True, text_color)
                text_rect = text_surface.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)


# -------------------------- 主程序入口 --------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    clock = pygame.time.Clock()

    grid = init_grid()
    score = 0

    while True:
        draw_game(screen, grid, score)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                old_grid = [row.copy() for row in grid]
                score_add = 0

                # 方向键控制
                if event.key == pygame.K_LEFT:
                    grid, score_add = move_left(grid)
                elif event.key == pygame.K_RIGHT:
                    grid, score_add = move_right(grid)
                elif event.key == pygame.K_UP:
                    grid, score_add = move_up(grid)
                elif event.key == pygame.K_DOWN:
                    grid, score_add = move_down(grid)
                else:
                    continue

                # 有效移动才加分、生成新方块
                if is_grid_changed(old_grid, grid):
                    score += score_add
                    add_new_tile(grid)

                    if is_game_over(grid):
                        print(f"游戏结束！最终得分：{score}")
                        pygame.quit()
                        sys.exit()

        clock.tick(60)


if __name__ == "__main__":
    main()