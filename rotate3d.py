
pred = model(xy_grid).detach().cpu()

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121, projection = '3d')
ax2 = fig.add_subplot(122,projection = '3d')

def rotate_fig(angle):
    ax1.view_init(azim=angle)
    ax2.view_init(azim=angle)

surf = ax1.scatter(xx_true, yy_true, zz_true.view(-1,1), c= zz_true, s = 1, label="True Green function of dirac delta")
surf2 = ax2.scatter(xx_true, yy_true, pred.view(-1,1), c= pred, s = 1, label = "Prediction")

rot_animation = animation.FuncAnimation(fig, rotate_fig, frames=np.arange(0,362,2),interval=100)

fig.colorbar(surf)
fig.colorbar(surf2)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

ax2.set_xlabel('x axis')
ax2.set_ylabel('y axis')
ax2.set_zlabel('z axis')

plt.legend()
plt.tight_layout()
rot_animation.save(save_figure_path + f"ouput_ani_{exp_index}.gif")
plt.show()
