<template>
  <div id="app">

    <form @submit.prevent="createRecord">
      <div class="col-md-6 offset-md-3">
        <input type="text" class="form-control col-3 mx-2" placeholder="Логин работника" v-model="record.employee_name"><br/>
        <input type="text" class="form-control col-3 mx-2" placeholder="Наименование сырья" v-model="record.raw_material_name"><br/>
        <input type="text" class="form-control col-3 mx-2" placeholder="Содержание железа" v-model="record.iron_concentration"><br/>
        <input type="text" class="form-control col-3 mx-2" placeholder="Содержание кремния" v-model="record.silicon_concentration"><br/>
        <input type="text" class="form-control col-3 mx-2" placeholder="Содержание алюминия" v-model="record.aluminum_concentration"><br/>
        <input type="text" class="form-control col-3 mx-2" placeholder="Содержание кальция" v-model="record.calcium_concentration"><br/>
        <input type="text" class="form-control col-3 mx-2" placeholder="Содержание серы" v-model="record.sulfur_concentration"><br/>
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Создано"><br/>-->
        <button type="submit" class="btn btn-success">Submit</button><br/>
      </div><br/>
    </form>

<!--    <form action="">-->
<!--      <div class="form-group column">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--        <input type="text" class="form-control col-3 mx-2" placeholder="Name">-->
<!--      </div>-->
<!--    </form>-->

    <table class="table table-striped table-hover table-bordered">
      <thead >
        <th>Логин работника</th>
        <th>Наименование сырья</th>
        <th>Содержание железа</th>
        <th>Содержание кремния</th>
        <th>Содержание алюминия</th>
        <th>Содержание кальция</th>
        <th>Содержание серы</th>
        <th>Создано</th>
        <th>iD</th>
      </thead>
      <tbody>
        <tr v-for="record in records" :key="record.id">
          <td>{{ record.employee_name }}</td>
          <td>{{ record.raw_material_name }}</td>
          <td>{{ record.iron_concentration }}%</td>
          <td>{{ record.silicon_concentration }}%</td>
          <td>{{ record.aluminum_concentration }}%</td>
          <td>{{ record.calcium_concentration }}%</td>
          <td>{{ record.sulfur_concentration }}%</td>
          <td>{{ record.created_at }}</td>
          <td><a href="{% url 'record' record.id %}">{{ record.id }}</a></td>
        </tr>
        </tbody>
    </table>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return {
      record: {
        'employee_name':'',
        // '':
        // '':
        // '':
        // '':
        // '':
        // '':
        // '':
      },
      records: []
    }
  },
  async created() {
    var response = await fetch('http://localhost:8000/api/record/');
    this.records = await response.json();
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
